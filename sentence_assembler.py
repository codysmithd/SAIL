

import ngram
from random import randint


def load():
	ngram.load()
		

def rateSentence(words):
	return ngram.rateSentence(words)

# make sentence using the supplied words
def run(structure, word_options):

	sentence = []

	print "==========================================="

	if len(word_options) >= len(structure):
		print structure

		# loop through word spots in the structure
		for pos in structure:
			print "position: " + str(len(sentence))
			print "part of speech: " + str(pos)

			# get the previous words in the sentence
			prev = getPrevious(sentence)

			print "previous: " + str(prev)

			# use ngrams to find the 
			best = findBest(prev, word_options, pos)

			print "best: " + str(best)

			# if nothing was found
			if best == -1:
				print "abort find----------"
				'''
				options = ngram.getNextWords(prev, pos)
				sentence.append(options[randint(0, len(options) - 1)])
				'''
				return ""

			else:
				# add the best word as the next word in the sentence
				sentence.append(word_options[best][0])

				# remove the word from the options
				word_options.pop(best)

	# convert to space seperated string
	sentence = " ".join(sentence)
	return sentence

def getPrevious(sentence):
	if len(sentence) >= 1:
		return sentence[-1]
	else:
		return "<s>"

def findBest(prev, word_options, pos):
	best_index = -1
	best_rating = 0
	for index, option in enumerate(word_options):

		# only look at word_options that are the right parts of speech
		if int(option[1]) == pos:

			# get the ngram rating for this word
			rating = ngram.getProb(prev, option[0])

			print prev + " " + option[0] + " = " + str(rating)

			# test if better
			if rating > best_rating:
				best_index = index
				best_rating = rating

	return best_index