

import json


bigram = None
unigram = None


def load():
	global bigram
	global unigram

	print("Loading N-gram databases...")

	f = open("datasets/bigram.json", 'r')
	bigram = json.load(f)
	f.close()

	f = open("datasets/unigram.json", 'r')
	unigram = json.load(f)
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
	global bigram
	if word1 in bigram:
		if word2 in bigram[word1]:
			if word3 in bigram[word1][word2]:
				return bigram[word1][word2][word3]
	return 0

def get_unigram_score(word1, word2):
	global unigram
	if word1 in unigram:
		if word2 in unigram[word1]:
				return unigram[word1][word2]
	return 0
