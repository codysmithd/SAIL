
import json

class sentence_assembler:

	def __init__(self):

		print "loading n-gram models..."

		f = open("datasets/ngram_backward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()

		f = open("datasets/ngram_forward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()

	# make sentence using the supplied nouns and verbs
	def run(self, nouns, verbs):
		pass

	def getSentenceProb(self, words):
		pass

	def getNextWords(self, word):
		pass

	def getPrevWords(self, word):
		pass
