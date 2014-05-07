
'''
Setup
'''

import os
import nltk
import structures
import sentence_assembler
from relational import relational_map


# inits
structures.load()
sentence_assembler.load()

print "loading long term memory"

long_term = relational_map()
long_term.load_from_file("long_term.txt.gzip")

print "done loading memory"


'''
Main loop
'''

def clearConsole():
	os.system(['clear','cls'][os.name == 'nt'])


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

		# get words from relationals
		seed_words = []
		for token in tagged_tokens:
			seed_words += long_term.get_top_links_for_word(token, 50)


		# choose a structure
		struct = structures.getRandom()

		# assemble sentence
		#print sentence_assembler.rateSentence(tagged_tokens)
		print sentence_assembler.run(struct, seed_words)[1]


clearConsole()
	