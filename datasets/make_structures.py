

import json


'''
load the corpus
'''

blackList = [18, 19, 24, 28, 33, 34, 35]

def isLegal(t):
	global blackList
	for pos in t:
		if pos in blackList:
			return False
	return True

print("loading JSON corpus")

f = open("tagged_corpus.json", 'r')
if(f):
	sentences = json.load(f)
else:
	print("no corpus file")
	input() # hold for user
f.close()


print("compiling structures")

struct_dict = {}
total_sents = len(sentences)
count = 0

for sentence in sentences:
	count += 1
	if count % 50 == 0:
		print(str(count) + " of " + str(total_sents))
	
	l = []
	for word in sentence:
		l.append(word[1])
	t = tuple(l)
	if len(t) <= 6 and len(t) >= 4:
		if isLegal(t):
			# add it if it's not already there
			t_string = str(t)

			if t_string not in struct_dict:
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
structures = structures[0:40]

# eliminate the count variable
for index, value in enumerate(structures):
	structures[index] = value[1]


print(structures)


print("building JSON...")

# dump it
f = open("corpus_structures.json", 'w')
json.dump(structures, f)
f.close()

print(str(len(structures)))

print("DONE!")

input()
