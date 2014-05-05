

import json


ngram_backward = None
ngram_forward = None
parts_of_speech = None


def load():
	global ngram_backward
	global ngram_forward
	global parts_of_speech

	print "1 of 3"
	f = open("datasets/ngram_backward.json", 'r')
	ngram_backward = json.load(f)
	f.close()

	print "2 of 3"
	f = open("datasets/ngram_forward.json", 'r')
	ngram_forward = json.load(f)
	f.close()

	print "3 of 3"
	f = open("datasets/pos_tags.json", 'r')
	parts_of_speech = json.load(f)
	f.close()


def rateSentence(words):
	global ngram_backward

	rating = 0
	prev1 = "<s>"
	prev2 = "<s>"

	# backward ngrams
	for index, word in enumerate(words):
		if index >= 1:
			if ngram_backward.has_key(word):
				if ngram_backward[word].has_key(prev1):
					if ngram_backward[word][prev1].has_key(prev2):
						rating += ngram_backward[word][prev1][prev2][0]
		prev2 = prev1
		prev1 = word
	return rating



def getNextWords(word):
	global ngram_forward

	if ngram_forward.has_key(word):
		return ngram_forward[word].keys()
	else:
		return None

def getPrevWords(word):
	global ngram_backward

	if ngram_backward.has_key(word):
		return ngram_backward[word].keys()
	else:
		return None