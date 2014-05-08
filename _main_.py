
'''
Setup
'''

import os
import sys
import structures
import sentence_assembler
from relational import relational_map
from relational_short_term import short_term_relational


# nltk import gaurds
try:
	import nltk
except:
	print "Please install NLTK"
	raw_input() # wait for user
	sys.exit()

try:
	nltk.pos_tag(["asdf", "asdf"])
except:
	print "NLTK requires maxent_treebank_pos_tagger to continue."
	print "In the python console, run the following:"
	print ">>> import nltk"
	print ">>> nltk.download()"
	raw_input() # wait for user
	sys.exit()


# inits
structures.load()
sentence_assembler.load()

print "Creating short term memory..."
short_term = short_term_relational()

print "Loading long term memory..."

long_term = relational_map()
long_term.load_from_file("long_term.txt.gzip")

print "Ready..."


'''
Main loop
'''

def clearConsole():
	os.system(['clear','cls'][os.name == 'nt'])

def removeDuplicates(options):
	s = set()
	for word in options:
		s.add(word)
	return list(s)


clearConsole()


running = True
exit_words = ["done", "exit", "quit"]
remove_chars = [".", "," ,"\"", "\'", "?", ";"]

while running:
	user_input = raw_input(">>> ").lower()

	if user_input in exit_words:
		running = False
	else:

		# tokenize
		tokens = nltk.word_tokenize(user_input)

		# filter out punctuation
		tokens = [x for x in tokens if x not in remove_chars]

		# filter for nouns and verbs
		tagged_tokens = nltk.pos_tag(tokens)

		#convert pos to IDs
		tagged_tokens = structures.convertPos(tagged_tokens)

		# add the users words to the short term memory
		short_term.link_words(tagged_tokens)

		# get words from relationals
		primary_pos_tags = [1, 2, 4, 5, 6, 7, 8, 12, 13, 14, 16]
		primary_seeds = []
		secondary_seeds = []

		# Loops through users words
		for token in tagged_tokens:

			# get the top links for this token
			top_links = long_term.get_top_links_for_word(token, 50)
			top_links += short_term.get_top_links_for_word(token, 50)

			# sort the new words based on part-of-speech priority
			if token[1] in primary_pos_tags:
				primary_seeds += top_links
			else:
				secondary_seeds += top_links

		# remove duplicates
		primary_seeds = removeDuplicates(primary_seeds)
		secondary_seeds = removeDuplicates(secondary_seeds)


		result = ""
		count = 20
		while (result == "") and (count > 0):

			# choose a structure
			struct = structures.getRandom()
			print "choose structure: " + str(struct)

			# assemble sentence
			result = sentence_assembler.run(struct, primary_seeds, secondary_seeds)

			count -= 1
		
		print result

		# Ask if this result makes sense TODO


clearConsole()
	