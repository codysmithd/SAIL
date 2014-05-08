'''
This file builds the JSON bigram files.
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

backward_bigram = dict()

for sentence in sentences:

	prev1 = "<s>"
	prev2 = "<s>"

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not backward_bigram.has_key(word):
			backward_bigram[word] = dict()

		if not backward_bigram[word].has_key(prev1):
			backward_bigram[word][prev1] = dict()

		if not backward_bigram[word][prev1].has_key(prev2):
			backward_bigram[word][prev1][prev2] = [0, []]	

		backward_bigram[word][prev1][prev2][0] += 1

		if pos not in backward_bigram[word][prev1][prev2][1]:
			backward_bigram[word][prev1][prev2][1].append(pos)

		prev2 = prev1
		prev1 = word

	# add the ending marker
	word = "</s>"

	if not backward_bigram.has_key(word):
		backward_bigram[word] = dict()

	if not backward_bigram[word].has_key(prev1):
		backward_bigram[word][prev1] = dict()

	if not backward_bigram[word][prev1].has_key(prev2):
		backward_bigram[word][prev1][prev2] = [0, []]	

	backward_bigram[word][prev1][prev2][0] += 1

	if pos not in backward_bigram[word][prev1][prev2][1]:
		backward_bigram[word][prev1][prev2][1].append(pos)




print "building JSON..."

# dump it
f = open("bigram_backward.json", 'w')
json.dump(backward_bigram, f)
f.close()



'''
Build forward model
'''

print "building forward model..."

forward_bigram = dict()

for sentence in sentences:

	prev1 = "<s>"
	prev2 = "<s>"

	for tagged_token in sentence:

		word = tagged_token[0]
		pos = tagged_token[1]

		if not forward_bigram.has_key(prev2):
			forward_bigram[prev2] = dict()

		if not forward_bigram[prev2].has_key(prev1):
			forward_bigram[prev2][prev1] = dict()

		if not forward_bigram[prev2][prev1].has_key(word):
			forward_bigram[prev2][prev1][word] = [0, []]	

		forward_bigram[prev2][prev1][word][0] += 1

		if pos not in forward_bigram[prev2][prev1][word][1]:
			forward_bigram[prev2][prev1][word][1].append(pos)

		prev2 = prev1
		prev1 = word

	word = "</s>"

	if not forward_bigram.has_key(prev2):
		forward_bigram[prev2] = dict()

	if not forward_bigram[prev2].has_key(prev1):
		forward_bigram[prev2][prev1] = dict()

	if not forward_bigram[prev2][prev1].has_key(word):
		forward_bigram[prev2][prev1][word] = [0, []]	

	forward_bigram[prev2][prev1][word][0] += 1

	if pos not in forward_bigram[prev2][prev1][word][1]:
		forward_bigram[prev2][prev1][word][1].append(pos)



print "building JSON..."

# dump it
f = open("bigram_forward.json", 'w')
json.dump(forward_bigram, f)
f.close()

print "DONE!"
