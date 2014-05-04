
import json

class sentence_assembler:

	def __init__(self):

		print "loading n-gram models..."
		
		f = open("datasets/ngram_backward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()
		
		print "1 of 4"

		f = open("datasets/ngram_backward_pos.json", 'r')
		self.ngram_backward_pos = json.load(f)
		f.close()

		print "2 of 4"

		f = open("datasets/ngram_forward.json", 'r')
		self.ngram_backward = json.load(f)
		f.close()

		print "3 of 4"
		
		f = open("datasets/ngram_forward_pos.json", 'r')
		self.ngram_backward_pos = json.load(f)
		f.close()

		print "4 of 4"

	# make sentence using the supplied nouns and verbs
	def run(self, nouns, verbs):
		pass

	def getSentenceProb(self, words):
		pass

	def getNextWords(self, word):
		pass

	def getPrevWords(self, word):
		pass
