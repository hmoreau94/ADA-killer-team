import sys,os,time,random,pickle
from timeit import default_timer as timer
import pandas as pd
import numpy as np

try:
    from amazon.api import AmazonAPI
except ImportError:
    raise ImportError('Run : pip install python-amazon-simple-product-api')

sys.path.append('scripts/')
from data_import import *
from similarities import *
from utils import *

def get_details(x,name_feature,details_dict):
    details = details_dict.get(x.name) 
    if(details):
        return details.get(name_feature)
    else:
        return np.nan

def fill_in_with_details(book_desc_titles,amazon_access_file_path,get_candidate,dump_path):
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
            print("It took {} to get the data.".format(print_time(end - start,3)))
            return df,failed_list
    
    asin_in_get_candidate = list(get_candidate.keys())
    for id_ in get_candidate.keys():
        asin_in_get_candidate += get_candidate[id_]
    asin_in_get_candidate = set(asin_in_get_candidate)
    total_entries = len(asin_in_get_candidate)
    print("We have {} different asins in our candidate duplicates dictionnary.".format(total_entries))

    # Amazon login
    Access_key_ID,Secret_access_key,Associat_tag = pickle.load(open(amazon_access_file_path, "rb"))
    amazon = AmazonAPI(Access_key_ID, Secret_access_key, Associat_tag, Region ='FR', MaxQPS=0.9)

    # We create a dataframe that only contains those products
    book_only_candidates = book_desc_titles[book_desc_titles.index.isin(asin_in_get_candidate)]

    details_dict = {}
    failed = []
    error_count = 0
    for idx,id_ in enumerate(list(asin_in_get_candidate)):
        for attempt in range(100):
            try:
                p = amazon.lookup(ItemId=id_)
            except AsinNotFound :
                # The item was not found by the API
                failed.append(id_)
                break 
            except:
                # Most probably we are limited by the API in the number of requests
                error_count += 1
                time.sleep(1)
                continue
            else:
                # We have successfully retrieved the info
                break
        else:
            # We have failed all the attemps
            failed.append(id_)
        # Get the details
        details = { 'authors':p.authors,
                    'isbn':p.isbn,
                    'eisbn':p.eisbn,
                    'brand':p.brand,
                    'edition':p.edition,
                    'publisher':p.publisher
                  }
        details_dict[id_]= details
        progress(idx+1,total_entries,"Fetching from API (exceptions : {})".format(error_count))
    
    #Then we fill in the details in the dataframe
    book_only_candidates['authors'] = book_only_candidates.apply(lambda x : get_details(x,'authors',details_dict),axis=1)
    book_only_candidates['isbn'] = book_only_candidates.apply(lambda x : get_details(x,'isbn',details_dict),axis=1)
    book_only_candidates['eisbn'] = book_only_candidates.apply(lambda x : get_details(x,'eisbn',details_dict),axis=1)
    book_only_candidates['brand'] = book_only_candidates.apply(lambda x : get_details(x,'brand',details_dict),axis=1)
    book_only_candidates['edition'] = book_only_candidates.apply(lambda x : get_details(x,'edition',details_dict),axis=1)
    book_only_candidates['publisher'] = book_only_candidates.apply(lambda x : get_details(x,'publisher',details_dict),axis=1)
    
    end = timer()
    print("\nIt took {} to import the data.".format(print_time(end - start,3)))
    
    # We serialize it using pickle so that we do not have to download it again
    book_only_candidates.to_pickle(complete_path_dump)
    pickle.dump(failed, open(complete_path_failed, "wb"))
    print("Saved at : \n\t{}\n\t".format(complete_path_dump,complete_path_failed))
    print("{} failed retrieval(s) (check the returned list for more details)".format(len(failed)))
    
    return book_only_candidates,failed