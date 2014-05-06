import json
from relational import relational_map

# Open corpus
f = open("datasets/tagged_corpus.json", 'r')
sentences = json.load(f)
f.close()

# Make new relational map
long_term = relational_map()

n = 0

for sentence in sentences:
	words_pos = []
	for tuples in sentence:
		words_pos.append( (tuples[0],str(tuples[1])) )
	long_term.link_words(words_pos)
	print("\nSentence " + str(n) + " done\n")
	n += 1

long_term.output_file("output.txt")