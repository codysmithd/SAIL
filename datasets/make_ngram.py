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
prev = "<s>"

for sentence in sentences:

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not backward_ngram.has_key(word):
			backward_ngram[word] = dict()

		if not backward_ngram[word].has_key(prev):
			backward_ngram[word][prev] = [0, []]	

		backward_ngram[word][prev][0] += 1

		if pos not in backward_ngram[word][prev][1]:
			backward_ngram[word][prev][1].append(pos)

		prev = word


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
prev = "</s>"

for sentence in sentences:

	reversedSent = list(sentence)
	reversedSent.reverse()

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not forward_ngram.has_key(word):
			forward_ngram[word] = dict()

		if not forward_ngram[word].has_key(prev):
			forward_ngram[word][prev] = [0, []]	

		forward_ngram[word][prev][0] += 1

		if pos not in forward_ngram[word][prev][1]:
			forward_ngram[word][prev][1].append(pos)

		prev = word



print "building JSON..."

# dump it
f = open("ngram_forward.json", 'w')
json.dump(forward_ngram, f)
f.close()

print "DONE!"
