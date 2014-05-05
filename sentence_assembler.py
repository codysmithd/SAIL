

import ngram


class sentence_assembler:

	def __init__(self):

		print "loading n-gram models..."
		ngram.load()
		

	# make sentence using the supplied nouns and verbs
	def run(self, tagged_tokens):
		words = []
		for token in tagged_tokens:
			words.append(token[0])

		return ngram.rateSentence(words)
