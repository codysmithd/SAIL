
import json # json, I choose you
from nltk.corpus import brown



'''
Preprocess tokens
'''

remove = ["\"", "\'", "\'\'", ",", ":", "`", "``", "(", ")"]
fullstop = ["?", ";"]

words = brown.words()
print "total words: " + str(len(words))

# ditch all punctuation except periods
words = [x for x in words if x not in remove]

# convert other punctuation to periods
words = ["." if word in fullstop else word for word in words]

print "without punctuation: " + str(len(words))



# split into sentences

sentences = []
current = []

for word in words:
	if word == ".":
		sentences.append(current)
		current = []
	else:
		current.append(word.lower())

print "sentences: " + str(len(sentences))






'''
Build model
'''

print "building model..."

backward_ngram = dict()
prevWord = None

for sentence in sentences:
	for word in sentence:

		if not backward_ngram.has_key(word):
			backward_ngram[word] = dict()

		if prevWord == None:
			prevWord = "<s>"

		if not backward_ngram[word].has_key(prevWord):
			backward_ngram[word][prevWord] = 0

		backward_ngram[word][prevWord] += 1

		prevWord = word



print "building JSON..."

# dump it
f = open("ngram_model_backward.json", 'w')
json.dump(backward_ngram, f)
f.close()

print "DONE!"


raw_input()
