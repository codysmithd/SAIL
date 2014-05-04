'''
This file parses the Brown corpus, tags parts of speech, and puts out a JSON file for the corpus.
It takes a while...
'''


import json
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
Part of speech tagging
'''

print "tagging parts of speech..."

counter = 0
for index, sentence in enumerate(sentences):
	#because it takes so long
	counter += 1
	if counter % 50 == 0:
		print str(counter) + " of " + str(total_sents)

	sentences[index] = nltk.pos_tag(sentence)


print "building JSON..."

# dump it
f = open("tagged_corpus.json", 'w')
json.dump(sentences, f)
f.close()

print "DONE!"
