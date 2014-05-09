'''
This file builds the JSON unigram files.
'''


#locks to prevent accidental execution

import json
import nltk

unigram = dict()

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




def add(word1, word2):
	global unigram

	if not unigram.has_key(word1):
		unigram[word1] = dict()

	if not unigram[word1].has_key(word2):
		unigram[word1][word2] = 0

	unigram[word1][word2] += 1



'''
Build backward model
'''

print "building backward model..."

for sentence in sentences:

	word1 = "<s>"

	for word2 in sentence:
		word2 = word2[0]

		add(word1, word2)

		# walk the buffers
		word1 = word2


	# add the FIRST ending marker
	word2 = "</s>"

	add(word1, word2)

	# walk the buffers
	word1 = word2


	# add the SECOND ending marker
	word2 = "</s>"

	add(word1, word2)

	# walk the buffers
	word1 = word2


print "building JSON..."

# dump it
f = open("unigram.json", 'w')
json.dump(unigram, f)
f.close()



print "DONE!"

raw_input()
