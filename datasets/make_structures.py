

import json


'''
load the corpus
'''

print "loading JSON corpus"

f = open("tagged_corpus.json", 'r')
if(f):
	sentences = json.load(f)
else:
	print "no corpus file"
	raw_input() # hold for user
f.close()


print "compiling structures"

structures = []
total_sents = len(sentences)
count = 0

for sentence in sentences:
	count += 1
	if count % 50 == 0:
		print str(count) + " of " + str(total_sents)
	
	l = []
	for word in sentence:
		l.append(word[1])
	t = tuple(l)
	if t not in structures:
		structures.append(t)
	else:
		print "repeat"



print "building JSON..."

# dump it
f = open("corpus_structures.json", 'w')
json.dump(structures, f)
f.close()


print "DONE!"

raw_input()
