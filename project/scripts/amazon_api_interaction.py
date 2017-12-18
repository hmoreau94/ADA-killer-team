import sys,os,time,random,pickle,math
from timeit import default_timer as timer
import pandas as pd
import numpy as np


try:
    from amazon.api import AmazonAPI
    from amazon.api import LookupException, AsinNotFound
except ImportError:
    raise ImportError('Run : pip install python-amazon-simple-product-api')

try:
    import isbnlib
except ImportError:
    raise ImportError('Run : pip install isbnlib')

from scripts.similarities import *
from scripts.analysis import *
from scripts.data_import import *
from scripts.utils_project import *


def retriever_amazon(x,amazon,max_trials):
    products = None
    for attempt in range(max_trials):
        try:
            products = amazon.lookup_bulk(ItemId=x)
        except:
            # Most probably we are limited by the API in the number of requests
            time.sleep(random.expovariate(0.1))
            continue
        else:
            # We have successfully retrieved the info
            break
    else:
        # We have failed all the attempts, is called if the for loop never encounters a break
        return None,None
    if(products):
        failed_asin = []
        asin2details = {}
        for p in products:
            asin2details[p.asin]={  'Authors':p.authors,
                                    'Publisher':p.publisher,
                                    'ISBN':p.isbn,
                                    'Sales Rank':p.sales_rank,
                                    'Binding':p.binding,
                                    'Edition':p.edition,
                                    'Release Date':p.release_date}
        failed_asin = [i for i in x.split(',') if (i not in asin2details.keys())]
        return failed_asin,asin2details

def get_details(x,name_feature,details_dict):
    """
    Returns the detail 'name_feature' stored in the dictionnary itself stored in details_dict.
    In case of failure it will return np.nan

    @params:
    - x a dataframe serie which name attribut corresponds to the key of details_dict
    - name_feature is the name of the detail feature we want to obtain for x
    - details_dict is a dictionnary containing ASINs as keys and detail dictionnaries as values
    """
    details = details_dict.get(x['asin']) 
    if(details):
        return details.get(name_feature)
    else:
        return np.nan

def fill_in_with_details(book_desc_titles,amazon_access_file_path,candidate_dict,asin_2_similarity_list,dump_path):
    """
    Will return the extra details that can be fetched fromn the amazon API for all the rows in book_desc_titles.
    It will not call the API if there is already a dump of this operation (to avoid calling it too often)

    @params:
    - book_desc_titles : a dataframe which contains all books of interest with the information we decided to keep from the dataset after the first import.
    - amazon_access_file_path : the path to a pickled version of the amazon access credition
    - candidate_dict : a dictionnary associating book asins to a list of asins which books are candidate similars
    - dump_path : the path to the folder where the dump should be saved
    """

    start = timer()
    complete_path_dump = dump_path + "book_only_candidates_with_details"
    complete_path_failed = dump_path + "api_failed"
    
    # Get the file from the dump
    if(os.path.isfile(complete_path_dump)):
        if(os.path.isfile(complete_path_failed)):
            print("Retrieving from : \n\t{}\n\t{} ".format(complete_path_dump,complete_path_failed))
            df = pd.read_pickle(complete_path_dump)
            failed_list = pickle.load(open(complete_path_failed, "rb"))
            end = timer()
            print("It took {} to get the data.".format(human_readible_time(end - start,3)))
            return df,failed_list

    total_entries = len(asin_2_similarity_list)
    asin_in_get_candidate = list(asin_2_similarity_list.keys())
    print("We have {} different asins in our candidate duplicates dictionnary.".format(total_entries))

    Access_key_ID,Secret_access_key,Associat_tag = pickle.load(open(amazon_access_file_path, "rb"))
    amazon = AmazonAPI(Access_key_ID, Secret_access_key, Associat_tag, Region ='FR', MaxQPS=0.9)
    retriever_amz = (lambda x: retriever_amazon(x,amazon,100))
    
    # We create a dataframe that only contains those products
    book_desc_titles = book_desc_titles.reset_index()
    book_only_candidates = book_desc_titles[book_desc_titles['asin'].isin(asin_in_get_candidate)]

    details_dict = {}
    failed = []
    error_count = 0
    upper_bound = math.ceil(total_entries/10)
    for i in range(0,upper_bound):
        # We retrieve the asins 10 by 10
        low = 10*i
        high = (10*i+9) if (10*i+9) < total_entries else total_entries-1
        asins = ",".join(asin_in_get_candidate[low:high+1])
        failed_asin,asin2details = retriever_amz(asins) 

        failed = failed + failed_asin

        details_dict.update(asin2details)
        progress(high,total_entries,"Fetching from API (failed : {})".format(len(failed)))
    
    #Then we fill in the details in the dataframe
    book_only_candidates['authors'] = book_only_candidates.apply(lambda x : get_details(x,'Authors',details_dict),axis=1)
    book_only_candidates['publisher'] = book_only_candidates.apply(lambda x : get_details(x,'Publisher',details_dict),axis=1)
    book_only_candidates['ISBN'] = book_only_candidates.apply(lambda x : get_details(x,'ISBN',details_dict),axis=1)
    book_only_candidates['sales_rank_updated'] = book_only_candidates.apply(lambda x : get_details(x,'Sales Rank',details_dict),axis=1)
    book_only_candidates['binding'] = book_only_candidates.apply(lambda x : get_details(x,'Binding',details_dict),axis=1)
    book_only_candidates['edition'] = book_only_candidates.apply(lambda x : get_details(x,'Edition',details_dict),axis=1)
    book_only_candidates['release_date'] = book_only_candidates.apply(lambda x : get_details(x,'Release Date',details_dict),axis=1)
    
    end = timer()
    print("\nIt took {} to import the data.".format(human_readible_time(end - start,3)))
    
    # We serialize it using pickle so that we do not have to download it again
    book_only_candidates.to_pickle(complete_path_dump)
    pickle.dump(failed, open(complete_path_failed, "wb"))
    print("Saved at : \n\t{}\n\t".format(complete_path_dump,complete_path_failed))
    print("{} failed retrieval(s) (check the returned list for more details)".format(len(failed)))
    
    return book_only_candidates,failed