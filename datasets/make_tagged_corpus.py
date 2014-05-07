'''
This file parses the Brown corpus, tags parts of speech, and puts out a JSON file for the corpus.
It takes a while...
'''

#locks to prevent accidental execution

import json
import nltk



'''
Preprocess tokens
'''

remove = ["", "-", "--", "pa", "af", "u", "wb", "n't"]
containRemove = ["\"", "\'", "\'\'", ",", ":", "`", "``", "*", "@", "#", "/", "\\", "<", ">", "+", "=", "|", "_", "~", "^", "%", "&", "(", ")", "[", "]", "{", "}"]
fullstop = ["?", ";", "!", "!!", "!!!", "..", "...", "....", "'."]

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

# returns boolean of whether it should be added to the corpus
def discriminate(x):
	if x in remove: # predefined list of stuff to ditch
		return False
	if (x[0] == "u") and is_number(x[1:]): # no weird unicode characters
		return False
	for test in containRemove: # test if the string contains anything illegal
		if test in x:
			return False
	return True

print "Loading words..."

words = nltk.corpus.brown.words()
words += nltk.corpus.nps_chat.words()

print "Total words: " + str(len(words))
print "Striping bad words..."

# ditch stuff
words = [x for x in words if discriminate(x)]

# convert other punctuation to periods
words = ["." if word in fullstop else word for word in words]

print "Total words: " + str(len(words))



'''
split into sentences
'''

print "Splitting into sentences"

sentences = []
current = []

for word in words:
	if word == ".":
		sentences.append(current)
		current = []
	else:
		current.append(word.lower())

total_sents = len(sentences)
print "Sentences: " + str(total_sents)




'''
Part of speech tagging
'''

print "Tagging parts of speech..."

parts = []
counter = 0

for index, sentence in enumerate(sentences):
	# because it takes so long
	counter += 1
	if counter % 50 == 0:
		print str(counter) + " of " + str(total_sents)

	# tag it
	sentences[index] = nltk.pos_tag(sentence)

	# replace tags with indexes of tag list (saves space/time later)
	for subIndex, token in enumerate(sentences[index]):
		token = list(token)

		if token[1] not in parts:
			parts.append(token[1])

		token[1] = parts.index(token[1])

		sentences[index][subIndex] = token


print "building JSON..."

# dump it
f = open("tagged_corpus.json", 'w')
json.dump(sentences, f)
f.close()

f = open("pos_tags.json", 'w')
json.dump(parts, f)
f.close()

print "DONE!"

raw_input()
