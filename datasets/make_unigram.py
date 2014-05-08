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

backward_unigram = dict()

for sentence in sentences:

	prev = "<s>"

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not backward_unigram.has_key(word):
			backward_unigram[word] = dict()

		if not backward_unigram[word].has_key(prev):
			backward_unigram[word][prev] = [0, []]

		backward_unigram[word][prev][0] += 1

		if pos not in backward_unigram[word][prev][1]:
			backward_unigram[word][prev][1].append(pos)

		prev = word

	# add the ending marker
	word = "</s>"

	if not backward_unigram.has_key(word):
		backward_unigram[word] = dict()

	if not backward_unigram[word].has_key(prev):
		backward_unigram[word][prev] = [0, []]

	backward_unigram[word][prev][0] += 1

	if pos not in backward_unigram[word][prev][1]:
		backward_unigram[word][prev][1].append(pos)


print "building JSON..."

# dump it
f = open("unigram_backward.json", 'w')
json.dump(backward_unigram, f)
f.close()



'''
Build forward model
'''

print "building forward model..."

forward_unigram = dict()

for sentence in sentences:

	prev = "<s>"

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not forward_unigram.has_key(prev):
			forward_unigram[prev] = dict()

		if not forward_unigram[prev].has_key(word):
			forward_unigram[prev][word] = [0, []]	

		forward_unigram[prev][word][0] += 1

		if pos not in forward_unigram[prev][word][1]:
			forward_unigram[prev][word][1].append(pos)

		prev = word

	# add the ending marker
	word = "</s>"

	if not backward_unigram.has_key(prev):
		backward_unigram[prev] = dict()

	if not backward_unigram[prev].has_key(word):
		backward_unigram[prev][word] = [0, []]

	backward_unigram[prev][word][0] += 1

	if pos not in backward_unigram[prev][word][1]:
		backward_unigram[prev][word][1].append(pos)



print "building JSON..."

# dump it
f = open("unigram_forward.json", 'w')
json.dump(forward_unigram, f)
f.close()

print "DONE!"
