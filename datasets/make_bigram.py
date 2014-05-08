'''
This file builds the JSON bigram files.
'''


#locks to prevent accidental execution

import json
import nltk

bigram = dict()

'''
Load corpus
'''

print "loading JSON corpus..."

# load the tagged corpus
f = open("tagged_corpus.json", 'r')
if(f):
	sentences = json.load(f)
else:
	print "no corpus file"
	raw_input() # hold for user
f.close()




def add(word1, word2, word3):
	global bigram

	if not bigram.has_key(word1):
		bigram[word1] = dict()

	if not bigram[word1].has_key(word2):
		bigram[word1][word2] = dict()

	if not bigram[word1][word2].has_key(word3):
		bigram[word1][word2][word3] = 0

	bigram[word1][word2][word3] += 1



'''
Build backward model
'''

print "building backward model..."

for sentence in sentences:

	word1 = "<s>"
	word2 = "<s>"

	for word3 in sentence:
		word3 = word3[0]

		add(word1, word2, word3)

		# walk the buffers
		word1 = word2
		word2 = word3


	# add the FIRST ending marker
	word3 = "</s>"

	add(word1, word2, word3)

	# walk the buffers
	word1 = word2
	word2 = word3


	# add the SECOND ending marker
	word3 = "</s>"

	add(word1, word2, word3)

	# walk the buffers
	word1 = word2
	word2 = word3


print "building JSON..."

# dump it
f = open("bigram.json", 'w')
json.dump(bigram, f)
f.close()



print "DONE!"

raw_input()
