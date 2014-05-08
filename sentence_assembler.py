

import ngram
import random


def load():
	ngram.load()
		

def rateSentence(words):
	return ngram.rateSentence(words)

# make sentence using the supplied words
def run(structure, primary_options, secondary_options):

	sentence = []

	print "==========================================="

	if len(primary_options) >= len(structure):
		print structure

		# loop through word spots in the structure
		for pos in structure:
			# get the previous words in the sentence
			prev = getPrevious(sentence)

			'''
			print "position: " + str(len(sentence))
			print "part of speech: " + str(pos)
			print "previous: " + str(prev)
			'''

			# use ngrams to find the
			print "primary find..."

			current_list = None

			best = findBest(prev, primary_options, pos)
			if best != -1:
				current_list = primary_options
			else:
				print "secondary find..."
				best = findBest(prev, secondary_options, pos)
				if best != -1:
					current_list = secondary_options


			if current_list != None:
				sentence.append(current_list[best][0])
				current_list.pop(best)
			else:
				print "abort find----------"
				'''
				options = ngram.getNextWords(prev, pos)
				sentence.append(random.choice(options))
				'''
				return ""


	# convert to space seperated string
	sentence = " ".join(sentence)
	return sentence

def getPrevious(sentence):

	prev1 = "<s>"
	prev2 = "<s>"

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
			rating = ngram.unigram(prev, option[0])

			# print prev + " " + option[0] + " = " + str(rating)

			# test if better
			if rating > best_rating:
				best_index = index
				best_rating = rating

	return best_index