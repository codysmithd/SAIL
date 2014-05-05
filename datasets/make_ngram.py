'''
This file builds the JSON ngram files.
'''


#locks to prevent accidental execution

import json
import nltk


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





'''
Build backward model
'''

print "building backward model..."

backward_ngram = dict()
prev1 = "<s>"
prev2 = "<s>"

for sentence in sentences:

	for index, word in enumerate(sentence):

		pos = word[1]
		word = word[0]

		if index >= 1:

			if not backward_ngram.has_key(word):
				backward_ngram[word] = dict()

			if not backward_ngram[word].has_key(prev1):
				backward_ngram[word][prev1] = dict()	

			if not backward_ngram[word][prev1].has_key(prev2):
				backward_ngram[word][prev1][prev2] = [0, []]

			backward_ngram[word][prev1][prev2][0] += 1

			if pos not in backward_ngram[word][prev1][prev2][1]:
				backward_ngram[word][prev1][prev2][1].append(pos)

		prev2 = prev1
		prev1 = word


print "building JSON..."

# dump it
f = open("ngram_backward.json", 'w')
json.dump(backward_ngram, f)
f.close()



'''
Build forward model
'''

print "building forward model..."

forward_ngram = dict()
prev1 = "<s>"
prev2 = "<s>"

for sentence in sentences:

	reversedSent = list(sentence)
	reversedSent.reverse()

	for index, word in enumerate(reversedSent):

		pos = word[1]
		word = word[0]

		if index >= 1:

			if not forward_ngram.has_key(word):
				forward_ngram[word] = dict()

			if not forward_ngram[word].has_key(prev1):
				forward_ngram[word][prev1] = dict()	

			if not forward_ngram[word][prev1].has_key(prev2):
				forward_ngram[word][prev1][prev2] = [0, []]

			forward_ngram[word][prev1][prev2][0] += 1

			if pos not in forward_ngram[word][prev1][prev2][1]:
				forward_ngram[word][prev1][prev2][1].append(pos)

		prev2 = prev1
		prev1 = word



print "building JSON..."

# dump it
f = open("ngram_forward.json", 'w')
json.dump(forward_ngram, f)
f.close()

print "DONE!"
