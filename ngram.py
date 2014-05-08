

import json


unigram_backward = None
unigram_forward = None


def load():
	global unigram_backward
	global unigram_forward

	print "Loading unigram databases..."

	f = open("datasets/unigram_backward.json", 'r')
	unigram_backward = json.load(f)
	f.close()
	

	f = open("datasets/unigram_forward.json", 'r')
	unigram_forward = json.load(f)
	f.close()



def rateSentence(words):

	rating = 0
	prev = "<s>"

	# backward unigrams
	for word in words:
		word = word[0]
		rating += getProb(prev, word)
		
		prev = word
	return rating



def unigram(prev, word):
	global unigram_backward
	if unigram_backward.has_key(word):
		if unigram_backward[word].has_key(prev):
				return unigram_backward[word][prev][0]
	return 0


def getNextWords(prev, pos):
	options = []
	if unigram_forward.has_key(prev):
		for tagged_token in unigram_forward[prev]:
			if tagged_token[1] == pos:
				print "abort find: " + tagged_token[0]
				options.append(tagged_token[0])
	return options


def queryForward(word):
	if unigram_forward.has_key(word):
		return unigram_forward[word]
	else:
		return None

def queryBackward(word):
	if unigram_backward.has_key(word):
		return unigram_backward[word]
	else:
		return None
