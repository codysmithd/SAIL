

import ngram
import random
import math


# globals

finished_sentences = []
max_rating = 0

sentence = []
structure = []
word_options = []


def load():
	ngram.load()


def removeDuplicates(options):
	s = set()
	for word in options:
		s.add(word)
	return list(s)


# make sentence using the supplied words
def run(struct, primary_options, secondary_options):
	global sentence
	global structure
	global word_options


	sentence = [""] * len(struct)
	structure = struct
	word_options = primary_options
	word_options = removeDuplicates(word_options)
	addWord(0)

	if len(finished_sentences) == 0:
		print "Secondary find"
		word_options += secondary_options
		word_options = removeDuplicates(word_options)
		addWord(0)


	print finished_sentences

	if len(finished_sentences) > 0:
		finished_sentences.sort(key=lambda tup: tup[1], reverse=True)
		return finished_sentences[0][0]
	else:
		return ""

# WARING: recursion
def addWord(i):
	global sentence
	global structure
	global word_options

	if i == len(structure):
		rateSentence()
	else:
		for word in word_options:
			if int(word[1]) == structure[i]:
				sentence[i] = word[0]
				addWord(i+1)



def rateSentence():
	global sentence
	global finished_sentences
	global max_rating

	rating = ngram.rateSentence(sentence)

	if rating[0] == max_rating:
		addSentence(rating[1])
	elif rating[0] > max_rating:
		max_rating = rating[0]
		finished_sentences = []
		addSentence(rating[1])

def addSentence(rating):
	global sentence
	global finished_sentences
	string = " ".join(sentence)
	return finished_sentences.append((string, rating))
