

import ngram


def load():
	ngram.load()
		

def rateSentence(words):
	return ngram.rateSentence(words)

# make sentence using the supplied words
def run(structure, word_options):
	result = 0
	sentence = []

	if len(word_options) < len(structure):
		result = -1
	else:
		print structure

		# loop through word spots in the structure
		for pos in structure:
			print "part of speech: " + str(pos)

			# get the previous words in the sentence
			prev = getPrevious(sentence)

			# use ngrams to find the 
			best = findBest(prev[0], prev[1], word_options, pos)

			# if anything was found
			if best == -1:
				result = -1
				break
			else:
				# add the best word as the next word in the sentence
				sentence.append(word_options[best][0])

				# remove the word from the options
				#word_options.pop(best)

	# convert to space seperated string
	sentence = " ".join(sentence)
	return (result, sentence)

def getPrevious(sentence):
	prev1 = "<s>"
	prev2 = "<s>"

	if len(sentence) >= 1:
		prev1 = sentence[-1]

	if len(sentence) >= 2:
		prev2 = sentence[-2]

	return (prev2, prev1)

def findBest(prev2, prev1, word_options, pos):
	best_index = -1
	best_rating = 0
	for index, option in enumerate(word_options):
		# only look at word_options that are the right parts of speech
		if option[1] == pos:
			# get the ngram rating for this word
			rating = ngram.getProb(prev2, prev1, option[0])
			# test if better
			if rating > best_rating:
				best_index = index
				best_rating = rating

	return best_index