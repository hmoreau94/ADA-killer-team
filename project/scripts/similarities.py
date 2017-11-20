import itertools,sys,os,pickle

from IPython.display import Image
from IPython.core.display import HTML 
from IPython.display import display

# externally downloaded dependencies
try :
    import unidecode
except ImportError:
    raise ImportError('Run : pip install unidecode')

try :
    import editdistance
except ImportError:
    raise ImportError('Run : pip install editdistance')

try:
    from termcolor import colored
except ImportError:
    raise ImportError('Run : conda install -c omnia termcolor')

try :
    from lsh import cache, minhash 
except ImportError:
    raise ImportError('Follow installation instruction for lsh at: https://github.com/mattilyra/lsh')


from data_import import *
from utils import *
from amazon_api_interaction import *


# =======================================================================================
#                                     Work on raw data
# =======================================================================================

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
        elif(p2 in get_candidate):
            get_candidate[p2].append(p1)
        else:
            get_candidate[p1] = []
            get_candidate[p1].append(p2)
    print("Found {} items with possible duplicates.".format(len(get_candidate)))

    # Saving to backup
    pickle.dump(get_candidate, open(dump_path, "wb"))

    return get_candidate

# =======================================================================================
#                                     Work on authors
# =======================================================================================

def clean_name(x):
    """Will clean the names of the authors, by performing the actions described below
    
    @params:
    - x : the string to clean
    """
    # get small latters
    x = x.lower()
    
    # delete accents
    x = unidecode.unidecode(x)
    
    # delete any space before or after string
    return x.strip()

def clean_name_in_dataframe(author_list):
    """ Cleans all the names in the author list of a given entry of our dataframe
    
    Rk : we also witnessed examples where authors names 
    """
    if(len(author_list) == 0):
        return []
    else:
        cleaned_authors = []
        for a in author_list:
            cleaned_authors.append(clean_name(a))
        return cleaned_authors        

def check_details_similarities(p_details,c_details,threshold,observational_print=False):
    """This function will try to find books that have the same authors"""
    p_authors = p_details['authors']
    c_authors = c_details['authors']
    if (p_authors == None or c_authors == None):
        return False
    if (len(p_authors) > 0 and len(c_authors) > 0):
        # We do have author lists that are both not empty
        return check_name_similarity(p_authors,c_authors,threshold,observational_print)

def check_name_similarity(authors1,authors2,threshold,observational_print=False):
    """
    Will check the similarity between two lists of authors. It uses the Levenstein distance made relative.
    It will look in the two lists what are the most probable matches (it looks at the match that minimises the metric describe below)

    Relative Levenstein = levenstein / maximum length between the two author names.
    Levenstein distance = number of edits to go from one string to another.

    @params:
    - authors1/2 = the two list of authors we whish to compare
    - threshold = the threshold under which we consider the levenstein distance to have found similar strings
    - observational_print = used to fine tune the proper threshold, it will print all the cases where the 
    threshold would have needed to be 25% higher to accept

    @returns:
    a boolean stating wether the two list can be considered similar.
    """
    # We take the longest list
    longuest,shortest = [authors1[:],authors2[:]] if (len(authors1) > len(authors2)) else [authors2[:],authors1[:]]
    # authors1[:] to copy them so that the remove later on doesn't affect the original list
    matched = []
    to_match_idx = 0
    while(len(shortest)>0 and to_match_idx < len(longuest)):
        distances = []
        to_match = longuest[to_match_idx]
        for a in shortest:
            # We make it relative so that we can use the same threshold for all strings
            max_length = len(to_match) if len(to_match) > len(a) else len(a)
            distances.append(editdistance.eval(to_match,a)/max_length)
        max_score_idx = np.argmin(distances)
        max_score = distances[max_score_idx]
        max_match = shortest[max_score_idx]
        matched.append((to_match,max_match,max_score))
        
        shortest.remove(max_match)
        to_match_idx += 1
        
    # now we have a list containing the matching of author names based on the max 
    # similarity scores. We decide to ignore the author names that are remaining 
    # (if they have more authors it could be that the first book didn't 
    # provide an exhaustive list of all authors)
    mean_score = np.mean([score for _,_,score in matched])
    are_similar = mean_score <= threshold
    if(observational_print and not are_similar and mean_score <= threshold*(1.25)):
        print("Not similar : {}".format(matched))
       
    return are_similar

def find_similarity_set(tuple,all_sets):
    for i,l in enumerate(all_sets):
        if(tuple[0] in l or tuple[1] in l):
            return i
    return -1

def get_similar_authors(book_only_candidates,get_candidate,threshold=0.35):
    """
    Looking at the candidate similar in get_candidate it will use the info in the dataframe book_only_candidates
    in order to determine if the authors are similar enough.
    """
    similars = []
    for primary in list(get_candidate.keys()):
        primary_details = book_only_candidates.loc[primary]
        candidates = get_candidate[primary]
        for c in candidates:
            candidate_details = book_only_candidates.loc[c]
            if(check_details_similarities(primary_details,candidate_details,threshold)):
                idx = find_similarity_set([primary,c],similars)
                if(idx == -1):
                    similars.append(set([primary,c]))
                else:
                    similars[idx].update([primary,c])
    similars = [sorted(list(s)) for s in similars]
    similars = {elements[0]:elements[1:] for elements in similars}

    return similars

# =======================================================================================
#                                     Work on titles
# =======================================================================================
def get_similar_titles(book_only_candidates,similars,observational_print=False):
    very_similars = []
    for primary in list(similars.keys()):
        p_title = book_only_candidates.loc[primary]['title']
        candidates = similars[primary]

        for c in candidates:
            c_title = book_only_candidates.loc[c]['title']
            dp,dc = get_difference(p_title,c_title)

            if(observational_print and len(dp)>0 and len(dc)>0):
                print("'{}'\n'{}'\n\t".format(p_title,c_title), colored("--->'{}','{}'".format(dp,dc),'red'))
            if(len(dp) == 0 and len(dc) == 0):
                # Insert the match in our list
                idx = find_similarity_set([primary,c],very_similars)
                if(idx == -1):
                    very_similars.append(set([primary,c]))
                else:
                    very_similars[idx].update([primary,c])
    very_similars = [sorted(list(s)) for s in very_similars]
    very_similars = {elements[0]:elements[1:] for elements in very_similars}
    return very_similars

def clean_title(x):
    """Will clean the titles
    
    @params:
    - x : the string to clean
    """
    x = x.lower() # get small letters
    x = unidecode.unidecode(x) # delete accents
    x = re.sub("[()]","",x) # delete parenthesis
    x = re.sub(r"(\s)\-(\s)", r"\1 \2",x) # dash between two spaces replace by nothing
    x = re.sub(r"([a-z]|[\d])\-([a-z]|[\d])", r"\1 \2",x) # dash between two strings replace by space 
    x = re.sub("[^(\w|\s)]","",x) # delete anything that isn't alphanumerical or a space
    
    # delete any space before or after string
    return x.strip()

def get_difference(s1,s2):
    """ 
    Will give the difference between two strings. 
    Returns the two strings where have been 
    deleted common words.
    
    @params:
    - s1,s2 : the two strings that we wish to compare
    
    """
    d1 = set([w for w in s1.split() if w not in s2])
    d2 = set([w for w in s2.split() if w not in s1])
    return " ".join(d1)," ".join(d2)


        