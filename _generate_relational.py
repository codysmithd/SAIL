import json
from relational import relational_map

print("Loading corpus")

# Open corpus
f = open("datasets/tagged_corpus.json", 'r')
sentences = json.load(f)
f.close()

print("Corpus loaded")

# Make new relational map
long_term = relational_map()

n = 0

print("\n")

for sentence in sentences:
	words_pos = []
	for tuples in sentence:
		words_pos.append( (str(tuples[0]),str(tuples[1])) )
	long_term.link_words(words_pos)
	print(("Sentence " + str(n) + " done"))
	n += 1

print("Outputting Text")
long_term.output_file("long_term.txt.gzip") # Output regular-text version

print("Done.")