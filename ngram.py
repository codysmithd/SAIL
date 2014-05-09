

import json


bigram = None


def load():
	global bigram

	print "Loading bigram database..."

	f = open("datasets/bigram.json", 'r')
	bigram = json.load(f)
	f.close()



def rateSentence(words):

	# copy, and add the end tags
	words = list(words)
	words.extend(("</s>", "</s>"))

	rating = 0
	total = 0

	word1 = "<s>"
	word2 = "<s>"

	for word3 in words:

		result = get_bigram_score(word1, word2, word3)
		rating += result

		if result > 0:
			total += 1

		# walk the buffers
		word1 = word2
		word2 = word3

	return (total, rating)


def get_bigram_score(word1, word2, word3):
	if bigram.has_key(word1):
		if bigram[word1].has_key(word2):
			if bigram[word1][word2].has_key(word3):
				return bigram[word1][word2][word3]
	return 0

def get_unigram_score(word1, word2):
	if bigram.has_key(word1):
		if bigram[word1].has_key(word2):
			if bigram[word1][word2].has_key(word3):
				return bigram[word1][word2][word3]
	return 0