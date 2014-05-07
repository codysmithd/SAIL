

import json


ngram_backward = None
ngram_forward = None


def load():
	global ngram_backward
	global ngram_forward

	print "Loading ngram databases..."

	f = open("datasets/ngram_backward.json", 'r')
	ngram_backward = json.load(f)
	f.close()
	

	f = open("datasets/ngram_forward.json", 'r')
	ngram_forward = json.load(f)
	f.close()



def rateSentence(words):

	rating = 0
	prev = "<s>"

	# backward ngrams
	for word in words:
		word = word[0]
		rating += getProb(prev, word)
		
		prev = word
	return rating



def getProb(prev, word):
	global ngram_backward
	if ngram_backward.has_key(word):
		if ngram_backward[word].has_key(prev):
				return ngram_backward[word][prev][0]
	return 0


def getNextWords(prev, pos):
	options = []
	if ngram_forward.has_key(prev):
		for tagged_token in ngram_forward[prev]:
			if tagged_token[1] == pos:
				print "abort find: " + tagged_token[0]
				options.append(tagged_token[0])
	return options


def query(word):
	if ngram_forward.has_key(word):
		return ngram_forward[word]
	else:
		return None
