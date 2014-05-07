

import json


ngram_backward = None
ngram_forward = None


def load():
	global ngram_backward
	global ngram_forward

	print "Loading ngram databases..."

	
	print "1 of 2"
	f = open("datasets/ngram_backward.json", 'r')
	ngram_backward = json.load(f)
	f.close()
	
	'''
	print "2 of 2"
	f = open("datasets/ngram_forward.json", 'r')
	ngram_forward = json.load(f)
	f.close()
	'''


def rateSentence(words):

	rating = 0
	prev1 = "<s>"
	prev2 = "<s>"

	# backward ngrams
	for word in words:
		word = word[0]
		rating += getProb(prev2, prev1, word)
		
		prev2 = prev1
		prev1 = word
	return rating



def getProb(prev2, prev1, word):
	global ngram_backward
	if ngram_backward.has_key(word):
		if ngram_backward[word].has_key(prev1):
			if ngram_backward[word][prev1].has_key(prev2):
				return ngram_backward[word][prev1][prev2][0]
	return 0
