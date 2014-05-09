

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
def run(struct, user_keywords, primary_words, secondary_words):
	global sentence
	global structure
	global word_options
	global finished_sentences
	global max_rating

	finished_sentences = []
	max_rating = 0
	sentence = [""] * len(struct)
	structure = struct
	word_options = primary_words
	word_options = removeDuplicates(word_options)
	addWord(0)

	if areValid():
		print "I'm still thinking..."
		finished_sentences = []
		max_rating = 0
		word_options += secondary_words
		word_options = removeDuplicates(word_options)
		addWord(0)


	#finished_sentences = keywordFilter(finished_sentences, user_keywords)

	if areValid():
		print finished_sentences
		finished_sentences.sort(key=lambda tup: tup[1], reverse=True)
		return finished_sentences[0][0]
	else:
		print "I'm sorry user, I'm afraid I can't respond to that..."
		return ""

# WARING: recursion
def addWord(i):
	global sentence
	global structure
	global word_options

	if i == len(structure):
		rateSentence()
	else:
		prev = "<s>"
		if i >= 1:
			prev = sentence[i - 1]

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

def keywordFilter(sentences, keywords):
	output = []
	for sentence in sentences:
		if hasKeyword(sentence, keywords):
			output.append(sentence)
	return output

def hasKeyword(sentence, keywords):
	for token in keywords:
		if token[0] in sentence[0]:
			return True
	return False

def areValid():
	global finished_sentences
	global structure
	global max_rating
	#  and (max_rating >= (len(structure) + 2 - 3))
	return (len(finished_sentences) > 0)
