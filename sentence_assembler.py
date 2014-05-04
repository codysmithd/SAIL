
import json

class sentence_assembler:

	def __init__(self):

		print "loading n-gram models..."
		print "1 of 2"

		f = open("datasets/ngram_backward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()

		print "2 of 2"
		'''
		f = open("datasets/ngram_forward.json", 'r')
		self.ngram_forward = json.load(f)
		f.close()
		'''
		

	# make sentence using the supplied nouns and verbs
	def run(self, tagged_tokens):
		words = []
		for token in tagged_tokens:
			words.append(token[0])

		return self.rateSentence(words)



	def rateSentence(self, words):
		rating = 0
		prev1 = "<s>"
		prev2 = "<s>"

		# backward ngrams
		for index, word in enumerate(words):

			if index >= 1:
				if self.ngram_backward.has_key(word):
					if self.ngram_backward[word].has_key(prev1):
						if self.ngram_backward[word][prev1].has_key(prev2):
							rating += self.ngram_backward[word][prev1][prev2][0]
			
			prev2 = prev1
			prev1 = word

		return rating



	def getNextWords(self, word):
		if self.ngram_forward.has_key(word):
			return self.ngram_forward[word].keys()
		else:
			return None

	def getPrevWords(self, word):
		if self.ngram_backward.has_key(word):
			return self.ngram_backward[word].keys()
		else:
			return None
