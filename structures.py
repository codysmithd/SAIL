

import json
import random

structures = None
pos_tags = None

def load():
	global structures
	global pos_tags

	print("Loading sentence structures...")
	f = open("datasets/corpus_structures.json", 'r')
	structures = json.load(f)
	f.close()

	print("Loading parts of speech...")
	f = open("datasets/pos_tags.json", 'r')
	pos_tags = json.load(f)
	f.close()

def getRandom():
	return random.choice(structures)

def convertPos(words):
	global pos_tags

	for index, word in enumerate(words):
		l = list(word)
		if l[1] in pos_tags:
			l[1] = pos_tags.index(l[1])
		else:
			l[1] = -1
		t = tuple(l)
		words[index] = t

	return words
	