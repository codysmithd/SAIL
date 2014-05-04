'''
This file builds the JSON ngram files.
'''


#locks to prevent accidental execution
'''
import json
import nltk
'''


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
prevWord = None

for sentence in sentences:

	for word in sentence:

		pos = word[1]
		word = word[0]

		if prevWord == None:
			prevWord = "<s>"

		if not backward_ngram.has_key(word):
			backward_ngram[word] = dict()

		if not backward_ngram[word].has_key(prevWord):
			backward_ngram[word][prevWord] = [0, []]

		backward_ngram[word][prevWord][0] += 1

		if pos not in backward_ngram[word][prevWord][1]:
			backward_ngram[word][prevWord][1].append(pos)

		prevWord = word


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
prevWord = None

for sentence in sentences:

	reversedSent = list(sentence)
	reversedSent.reverse()

	for word in reversedSent:

		pos = word[1]
		word = word[0]

		if prevWord == None:
			prevWord = "</s>"

		if not forward_ngram.has_key(word):
			forward_ngram[word] = dict()

		if not forward_ngram[word].has_key(prevWord):
			forward_ngram[word][prevWord] = [0, []]

		forward_ngram[word][prevWord][0] += 1

		if pos not in forward_ngram[word][prevWord][1]:
			forward_ngram[word][prevWord][1].append(pos)

		prevWord = word



print "building JSON..."

# dump it
f = open("ngram_forward.json", 'w')
json.dump(forward_ngram, f)
f.close()

print "DONE!"
