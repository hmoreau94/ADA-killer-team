import itertools,sys,os,pickle,copy
from timeit import default_timer as timer

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


from scripts.amazon_api_interaction import *
from scripts.analysis import *
from scripts.data_import import *
from scripts.utils_project import *



# =======================================================================================
#                                     Work on raw data
# =======================================================================================
def store_similars(asin1,asin2,similars,asin_2_similarity_list,next_id):
    """
    This function will store asin1 and asin2 in the same list and update similars,asin_2_similarity_list,next_id
    """
    index1 = asin_2_similarity_list.get(asin1,None)
    index2 = asin_2_similarity_list.get(asin2,None)
    if(index1!=None and index2!=None):
        # First we test if they are not already in the same bin
        if(index1!=index2):
            # We already have a similarity list for each asin, therefore we need to merge them
            # by default we keep p1 and add the list of p2
            similars[index1].update(similars[index2])
            # we update the list in which all asins similar to p2 are
            for asin in similars[index2]:
                asin_2_similarity_list[asin] = index1
            # we delete the old list of p2
            similars.pop(index2)
    
    else:
        idx = index1 if(index1!=None) else index2
        if(idx==None):
            # We update the dictionnary that remmembers where each asin has been put
            similars[next_id] = set([asin1,asin2])
            asin_2_similarity_list[asin1] = next_id
            asin_2_similarity_list[asin2] = next_id
            next_id = next_id + 1
        else:
            similars[idx].update([asin1,asin2])
            asin_2_similarity_list[asin1] = idx
            asin_2_similarity_list[asin2] = idx
    return similars,asin_2_similarity_list,next_id


def get_shingles(document,n_grams=5):
    """
    Returns the list of all n_grams that are in the document.

    @params:
    - document : the string representing the document
    - n_grams : the number of characters to be grouped together in our n_grams
    """
    return [document[head:head + n_grams] for head in range(0, len(document) - n_grams)]


def jaccard_dist(text1,text2):
    """
    Computes the jaccard distance between two lists.
    It is equal to the size of the intersection divided by size of the union

    @params:
    - text1,text2 : the two strings to compare
    """
    return len(set(text1) & set(text2)) / len(set(text1) | set(text2))

def get_fingerprint(x,hasher,lshcache,columns):
    """
    Will compute the fingerprint for the given entry based on the columns  
    we wish to use to create the description to be fingerprinted and save it in the lhscache

    @params:
    - x : the entry that for which we whish to obtain the fingerprint (where 'asin' is one of the column)
    - hasher : the hasher instance to use to compute the minhashes
    - lshcache : a cache instance to store the fingerprint
    - columns : the columns to use in the string on whish we will compute the fingerprint (e.g. ['title','description'])
    """
    fgprt = []
    for c in columns:
        fgprt.append(str(x[c]))

    to_fingerprint = " ".join(fgprt)
    fingerprint = hasher.fingerprint(to_fingerprint)
    lshcache.add_fingerprint(fingerprint, doc_id=x['asin'])

def candidate_duplicates(dataframe, dump_path, columns, char_ngram=2, seeds=100, bands=5, hashbytes=4):
    """
    Will compute the candidate duplicates from the passed dataframe.

    @params :
    - dataframe : the dataframe containing all the infos about books
    - dump_path : the path to the folder where the the result should be dumped or fetched if it already exists
    - char_ngram : the size of n-grams.
    - seeds : the number of minhashes that compose a document
    - bands : number of parts that divide each minhash
    """
    start = timer()  
    description_dump = [c for c in columns]
    description_dump += [str(x) for x in [char_ngram,seeds,bands,hashbytes]]
    suffix = "_".join(description_dump)
    dump_path_dup = dump_path + "candidate_dup_" + suffix
    dump_path_indexing_dict = dump_path + "indexing_dict_" + suffix

    if(os.path.isfile(dump_path_dup) and os.path.isfile(dump_path_indexing_dict) ):
        # Getting from backup
        print("Retrieving from :\n\t{}\n\t".format(dump_path_dup,dump_path_indexing_dict))
        get_candidate = pickle.load(open(dump_path_dup, "rb"))
        asin_2_similarity_list = pickle.load(open(dump_path_indexing_dict, "rb"))

        print("Found {} bins of possible duplicates.\nWith {} different books".format(len(get_candidate),len(asin_2_similarity_list)))
        end = timer()
        print("It took {} to import the data.".format(human_readible_time(end - start,3)))
        return get_candidate,asin_2_similarity_list


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
    end = timer()
    print("It took {} to detect duplicates.".format(human_readible_time(end - start,3)))

    similars = {}
    next_id = 0
    asin_2_similarity_list = {}
    for asin1,asin2 in list(candidate_pairs):
        similars,asin_2_similarity_list,next_id = store_similars(asin1,asin2,similars,asin_2_similarity_list,next_id)

    get_candidate = similars
    print("Found {} bins of possible duplicates.\nWith {} different books".format(len(get_candidate),len(asin_2_similarity_list)))

    # Saving to backup
    pickle.dump(get_candidate, open(dump_path_dup, "wb"))
    pickle.dump(asin_2_similarity_list, open(dump_path_indexing_dict, "wb"))

    return get_candidate,asin_2_similarity_list

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

    @params:
    - the list of authors we wish to clean
    """
    if(len(author_list) == 0):
        return []
    else:
        cleaned_authors = []
        for a in author_list:
            cleaned_authors.append(clean_name(a))
        return cleaned_authors        

def check_details_similarities(p_details,c_details,threshold,observational_print=False):
    """
    This function will try to find books that have the same authors based on the argument threshold

    @params:
    - p_details : the serie of details of the primary book
    - c_details : the serie of details of the candidate similar book
    - threshold : the threshold of the relative Levenstein distance under which books are considered similar
    - observational_print : allows to look at how the authors are compared. (see check_name_similarity for more details)
    """
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
    if(observational_print):
        for e in matched:
            print(e)
    if(observational_print and not are_similar and mean_score <= threshold*(1.25)):
        print("Not similar : {}".format(matched))
       
    return are_similar

def get_similar_authors(book_only_candidates,get_candidate,asin_2_similarity_list,threshold=0.35,observational_print=False):
    """
    Looking at the candidate similar in get_candidate it will use the info in the dataframe book_only_candidates
    in order to determine if the authors are similar enough.

    @params:
    - book_only_candidates : the dataframe containing all the books details only for books that are in get_candidate
    - get_candidate : a dictionnary that assigns to a primary ASIN all its candidate similars. It should be constructed 
    such that each book appears only once has a key or a value
    """

    # We can only work on books that have authors
    book_only_candidates = book_only_candidates.reset_index()
    book_only_candidates = book_only_candidates[book_only_candidates['authors'].notnull()]
    book_only_candidates = book_only_candidates[book_only_candidates['authors'].apply(lambda x:len(x)>0)]
    book_only_candidates['authors'] = book_only_candidates['authors'].apply(clean_name_in_dataframe)

    compliant_asins = set(book_only_candidates['asin'])
    all_asins = set(asin_2_similarity_list.keys())
    non_compliant_asins = all_asins - compliant_asins
    non_compliant_keys = set()
    for asin in non_compliant_asins:
        non_compliant_keys.add(asin_2_similarity_list[asin])

    candidate_compliant = copy.deepcopy(get_candidate)
    for key,s in get_candidate.items():
        inter = s & compliant_asins
        if(len(inter)<1):
            # the intersection is empty
            candidate_compliant.pop(key)
        else:
            candidate_compliant[key] = inter

    get_candidate = candidate_compliant
    book_only_candidates = book_only_candidates.reset_index().set_index('asin')
    lsh_to_author = {}
    similars = {}

    next_id = 0
    for key,similarity_bin in get_candidate.items():
        subsimilars = []
        details = [book_only_candidates.loc[asin] for asin in similarity_bin]
        for book1,book2 in itertools.combinations(details, 2):
            # we compare all the books 2 by 2
            if(check_details_similarities(book1,book2,threshold,observational_print)):
                # The two books are similar
                inserted = False
                for s in subsimilars:
                    if((book1.name in s or book2.name in s) and not inserted):
                        s.update([book1.name,book2.name])
                        inserted = True
                if(not inserted):
                    subsimilars.append(set([book1.name,book2.name]))

        # We have clustered all books with similar authors together inside subsimilars
        new_ids = []
        for c in subsimilars:
            new_ids.append(next_id)
            similars[next_id] = c
            next_id = next_id + 1

        # we keep track of where we place the new books after the author filtering
        lsh_to_author[key] = new_ids

    # we still need to add an empty list to the non_compliant_keys for consistency as they were not conserved after this step
    for k in non_compliant_keys:
        lsh_to_author[k] = []

    return similars,lsh_to_author

# =======================================================================================
#                                     Work on titles
# =======================================================================================
def get_similar_titles(book_only_candidates,similars,observational_print=False):
    """
    Will return a dictionnary which gives a correspondance to an ASIN and all the ASIN that are similar.
    It was designed such that an ASIN will appear only once as a key or a value. 

    @params :
    - book_only_candidates : a dataframe containing the book information 
        (both from the dataset and the API) that have at least one similar book.
    - similars : the correspondance from ASIN to the list of ASIN that are similar
    - Observational_print : can be set to True if once need to see how the method works
    """
    book_only_candidates = book_only_candidates.reset_index().set_index('asin')
    book_only_candidates['normalized_title'] = book_only_candidates['title'].apply(clean_title)
    
    authors_to_title = {}
    very_similars = {}
    next_id = 0

    for key,similarity_bin in similars.items():
        titles = [[asin,book_only_candidates.loc[asin]['normalized_title']] for asin in similarity_bin]
        subsimilars = []
        
        for pair1,pair2 in itertools.combinations(titles, 2):
            asin1,book1 = pair1
            asin2,book2 = pair2

            d1,d2 = get_difference(book1,book2)
            if(observational_print and len(d1)>0 and len(d2)>0):
                # Non empty difference, after cleaning the titles are still different
                print("'{}'\n'{}'\n\t".format(book1,book2), colored("--->'{}','{}'".format(d1,d2),'red'))
            if(len(d1) == 0 and len(d2) == 0):
                inserted = False
                for s in subsimilars:
                    if((asin1 in s or asin2 in s) and not inserted):
                        s.update([asin1,asin2])
                        inserted = True
                if(not inserted):
                    subsimilars.append(set([asin1,asin2]))

        # We have clustered all books with similar authors together inside subsimilars
        new_ids = []
        for c in subsimilars:
            new_ids.append(next_id)
            very_similars[next_id] = c
            next_id = next_id + 1

        # we keep track of where we place the new books after the author filtering
        authors_to_title[key] = new_ids
    return very_similars,authors_to_title

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
    words_1 = set(s1.split())
    words_2 = set(s2.split())
    d1 = set([w for w in words_1 if w not in words_2])
    d2 = set([w for w in words_2 if w not in words_1])
    return " ".join(d1)," ".join(d2)


        