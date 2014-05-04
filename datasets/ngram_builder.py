'''
This file builds the JSON ngram files.
'''


import json # json, I choose you
import nltk



'''
Preprocess tokens
'''

remove = ["\"", "\'", "\'\'", ",", ":", "`", "``", "(", ")"]
fullstop = ["?", ";"]

words = nltk.corpus.brown.words()
print "total words: " + str(len(words))

# ditch some punctuation
words = [x for x in words if x not in remove]

# convert other punctuation to periods
words = ["." if word in fullstop else word for word in words]

print "without punctuation: " + str(len(words))



'''
split into sentences
'''


sentences = []
current = []

for word in words:
	if word == ".":
		sentences.append(current)
		current = []
	else:
		current.append(word.lower())

total_sents = len(sentences)
print "sentences: " + str(total_sents)





'''
Build backward model
'''

print "building backward model..."

backward_ngram = dict()
prevWord = None

counter = 0

for sentence in sentences:

	#because it takes so long
	counter += 1
	if counter % 50 == 0:
		print str(counter) + " of " + str(total_sents)

	#tag the parts of speech
	parts_of_speech = nltk.pos_tag(sentence)

	for index, word in enumerate(sentence):

		pos = parts_of_speech[index][1]

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

		if not forward_ngram.has_key(word):
			forward_ngram[word] = dict()

		if prevWord == None:
			prevWord = "</s>"

		if not forward_ngram[word].has_key(prevWord):
			forward_ngram[word][prevWord] = 0

		forward_ngram[word][prevWord] += 1

		prevWord = word



print "building JSON..."

# dump it
f = open("ngram_forward.json", 'w')
json.dump(forward_ngram, f)
f.close()

print "DONE!"
