

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

struct_dict = {}
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
	if len(t) <= 20 and len(t) >= 6:
		# add it if it's not already there
		t_string = str(t)

		if not struct_dict.has_key(t_string):
			struct_dict[t_string] = [0, t]

		struct_dict[t_string][0] += 1


# put results in list

structures = []

for struct in struct_dict:
	struct = struct_dict[struct]
	structures.append(struct)

# sort for the highest, in descending order
structures.sort(key=lambda x: x[0], reverse=True)

# take the top x sentences
structures = structures[0:50]

# eliminate the count variable
for index, value in enumerate(structures):
	structures[index] = value[1]


print structures


print "building JSON..."

# dump it
f = open("corpus_structures.json", 'w')
json.dump(structures, f)
f.close()

print str(len(structures))

print "DONE!"

raw_input()
