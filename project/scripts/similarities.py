import itertools
import sys
import os
import pickle

from IPython.display import Image
from IPython.core.display import HTML 
from IPython.display import display
from amazon.api import AmazonAPI

# https://github.com/mattilyra/lsh
from lsh import cache, minhash 

sys.path.append('scripts/')
from data_import import *
from utils import *
from amazon_api_interaction import *


def get_shingles(document,n_grams=5):
    """
    Returns the list of all n_grams that are in the document.
    """
    return [document[head:head + n_grams] for head in range(0, len(document) - n_grams)]


def jaccard_dist(text1,text2):
    """
    Computes the jaccard distance between two lists.
    It is equal to the size of the intersection divided by size of the union
    """
    return len(set(text1) & set(text2)) / len(set(text1) | set(text2))

def get_fingerprint(x,hasher,lshcache,columns):
    """
    Will compute the fingerprint for the given entry based on the columns 
    we wish to use to create the description to be fingerprinted and save it in the lhscache
    """
    fgprt = []
    for c in columns:
        fgprt.append(str(x[c]))

    to_fingerprint = " ".join(fgprt)
    fingerprint = hasher.fingerprint(to_fingerprint)
    lshcache.add_fingerprint(fingerprint, doc_id=x['asin'])

def candidate_duplicates(dataframe, dump_path, columns, char_ngram=2, seeds=100, bands=5, hashbytes=4):
    """
    Will compute the candidate duplicates from the passed dataframe
    """
    description_dump = [c for c in columns]
    description_dump += [str(x) for x in [char_ngram,seeds,bands,hashbytes]]
    description_dump = "candidate_dup_" + "_".join(description_dump)
    dump_path = dump_path + description_dump

    if(os.path.isfile(dump_path)):
        # Getting from backup
        print("Retrieving from : {}".format(dump_path))
        get_candidate = pickle.load(open(dump_path, "rb"))
        print("Found {} items with possible duplicates.".format(len(get_candidate)))
        return get_candidate


    hasher = minhash.MinHasher(seeds=seeds, char_ngram=char_ngram, hashbytes=hashbytes)

    if seeds % bands != 0:
        raise ValueError('The number of bands must divide the seeds. {} % {} != 0'.format(seeds, bands))

    sys.stdout.write('Detecting potential candidates...')
    sys.stdout.flush()

    lshcache = cache.Cache(num_bands=bands, hasher=hasher)
    dataframe.reset_index().apply(lambda x : get_fingerprint(x,hasher,lshcache,columns),axis=1)

    candidate_pairs = set()
    for b in lshcache.bins:
        for bucket_id in b:
            if len(b[bucket_id]) > 1:
                pairs_ = set(itertools.combinations(b[bucket_id], r=2))
                candidate_pairs.update(pairs_)

    sys.stdout.write('Done...\r')
    sys.stdout.flush()

    # We then create a dictionnary that yields a list of asin that are similar to the key asin
    get_candidate = {}
    for p1,p2 in list(candidate_pairs):
        if(p1 in get_candidate):
            get_candidate[p1].append(p2)
        else:
            get_candidate[p1] = []
            get_candidate[p1].append(p2)
    print("Found {} items with possible duplicates.".format(len(get_candidate)))

    # Saving to backup
    pickle.dump(get_candidate, open(dump_path, "wb"))

    return get_candidate

def get_titles(asin,get_candidate, book_desc_titles):
    """returns the titles of all the candidate duplicates of a given asin in get_candidate"""
    title_desc_list = []
    title_desc_list.append(book_desc_titles.loc[asin]['title'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        title = entry['title']
        title_desc_list.append(title)
    return title_desc_list

def get_desc(asin,get_candidate, book_desc_titles):
    """returns the description of all the candidate duplicates of a given asin in get_candidate"""
    title_desc_list = []
    title_desc_list.append(book_desc_titles.loc[asin]['description'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        desc = entry['description']
        title_desc_list.append(desc)
    return title_desc_list

def display_images(asin,get_candidate, book_desc_titles):
    """Display the images of the candidate duplicates of a given asin in get_candidate"""
    url_list = []
    url_list.append(book_desc_titles.loc[asin]['imUrl'])
    for sim in get_candidate[asin]:
        entry = book_desc_titles.loc[sim]
        url = entry['imUrl']
        url_list.append(url)
    for link in url_list:
        display(Image(url=link))