
import json

class sentence_assembler:

	def __init__(self):

		print "loading n-gram models..."
		print "1 of 2"

		f = open("datasets/ngram_backward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()

		print "2 of 2"
		
		f = open("datasets/ngram_forward.json", 'r')
		self.ngram_forward = json.load(f)
		f.close()
		

	# make sentence using the supplied nouns and verbs
	def run(self, tagged_tokens):

		print self.getNextWords("the")


		words = []
		for token in tagged_tokens:
			words.append(token[0])

		return self.rateSentence(words)



	def rateSentence(self, words):
		rating = 0
		prevWord = "<s>"
		for word in words:
			if self.ngram_backward.has_key(word):
				if self.ngram_backward[word].has_key(prevWord):
					rating += self.ngram_backward[word][prevWord][0]
				else:
					rating -= 1
			else:
				rating -= 1

			prevWord = word

		return rating / len(words)



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
