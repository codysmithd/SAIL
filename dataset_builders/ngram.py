
import json # json, I choose you
from nltk.corpus import brown

remove = ["\"", "\'", "\'\'", ",", ":", "`", "``", "(", ")"]
fullstop = ["?", ";"]

print str(len(brown.sents()))

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

print sentences[0]



'''

ngram = set()
prevWord = None

for word in words:


	prevWord = word
'''



print "building JSON..."

# dump it
f = open("ngram_model.json", 'w')
json.dump(sentences, f)
f.close()

print "DONE!"



raw_input()
