

import ngram
import random
import math


def load():
	ngram.load()
		

def rateSentence(words):
	return ngram.rateSentence(words)

# make sentence using the supplied words
def run(structure, primary_options, secondary_options):

	sentence = []

	if len(primary_options) >= len(structure):

		# loop through word spots in the structure
		for pos in structure:
			# get the previous words in the sentence
			prev = getPrevious(sentence)

			'''
			print "position: " + str(len(sentence))
			print "part of speech: " + str(pos)
			print "previous: " + str(prev)
			'''

			current_list = None

			best = findBest(prev, primary_options, pos)
			if best != -1:
				current_list = primary_options
			else:
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
		prev1 = sentence[-1]
	if len(sentence) >= 2:
		prev2 = sentence[-2]

	return (prev1, prev2)

def findBest(prev, word_options, pos):

	best_index = -1
	best_rating = 0

	for index, option in enumerate(word_options):

		# only look at word_options that are the right parts of speech
		if int(option[1]) == pos:
			end = index == (len(word_options) - 1)
			rating = rateWord(prev, option, end)

			# test if better
			if rating > best_rating:
				best_index = index
				best_rating = rating

	return best_index



def rateWord(prev, word, end):

	prev1 = prev[0]
	prev2 = prev[1]

	if end:
		prev2 = prev1
		prev1 = word
		word = "</s>"

	# get the bigram rating for this word
	rating = ngram.bigram(prev2, prev1, word[0])

	
	if rating == 0:
		# get the unigram rating for this word
		rating = ngram.unigram(prev1, word[0])
	

	if rating != 0:
		# invert the rating
		rating *= -1
		rating += 1000

		# consider the strength of the relational linkage
		rating += int(word[2])

	# print prev + " " + word[0] + " = " + str(rating)
	return rating
