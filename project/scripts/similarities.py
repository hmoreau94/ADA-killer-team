import itertools
import sys
import os
import pickle

# https://github.com/mattilyra/lsh
from lsh import cache, minhash 


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

def get_fingerprint(x,hasher,lshcache):
	fingerprint = hasher.fingerprint(x['title'] + " " + x['description'])
	lshcache.add_fingerprint(fingerprint, doc_id=x['asin'])

def candidate_duplicates(dataframe, dump_path, char_ngram=5, seeds=100, bands=5, hashbytes=4):
	if(os.path.isfile(dump_path)):
		# Getting from backup
		print("Retrieving from : {}".format(dump_path))
		return pickle.load(open(dump_path, "rb"))


	hasher = minhash.MinHasher(seeds=seeds, char_ngram=char_ngram, hashbytes=hashbytes)

	if seeds % bands != 0:
		raise ValueError('The number of bands must divide the seeds. {} % {} != 0'.format(seeds, bands))

	sys.stdout.write('Detecting potential candidates...')
	sys.stdout.flush()

	lshcache = cache.Cache(num_bands=bands, hasher=hasher)
	dataframe.apply(lambda x : get_fingerprint(x,hasher,lshcache),axis=1)

	candidate_pairs = set()
	for b in lshcache.bins:
		for bucket_id in b:
			if len(b[bucket_id]) > 1:
				pairs_ = set(itertools.combinations(b[bucket_id], r=2))
				candidate_pairs.update(pairs_)

	sys.stdout.write('Done...\r')
	sys.stdout.flush()
	# Saving to backup
	pickle.dump(candidate_pairs, open(dump_path, "wb"))

	return candidate_pairs