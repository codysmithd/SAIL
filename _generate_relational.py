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
		words_pos.append( (str(tuples[0]),str(tuples[1])) )
	long_term.link_words(words_pos)
	print("Sentence " + str(n) + " done")
	print("(" + str(tuples[0]) + "," +str(tuples[1]) + ")")
	n += 1

print "Outputting Text"
long_term.output_file("output.txt") # Output regular-text version

#print "Outputting cPickle"
#with open("relational_pickle.data",'wb') as file_pointer:
    #pickle.dump(long_term,file_pointer)

print "Done."