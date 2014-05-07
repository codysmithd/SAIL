
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

print "Loading long term memory..."

long_term = relational_map()
long_term.load_from_file("long_term.txt.gzip")

print "Ready..."


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
		["DT", "NN", "VBD", "IN", "JJ", "VBN", "NNS", "RB", "WDT", "VBZ", "CC", "TO", "VB", "NNP", "VBG", "PRP", "VBP", "JJS", "CD", "MD", "JJR", "PRP$", "WRB", "EX", "LS", "WP", "RP", "RBR", "-NONE-", "RBS", "PDT", "WP$", "FW", ":", ".", "$", "``"]
		primary_pos_tags = [1, 2, 4, 5, 6, 7, 8, 12, 13, 14, 16]
		primary_seeds = []
		secondary_seeds = []

		for token in tagged_tokens:
			# get the top links for this token
			top_links = long_term.get_top_links_for_word(token, 50)

			# sort the new words based on part-of-speech priority
			if token[1] in primary_pos_tags:
				primary_seeds += top_links
			else:
				secondary_seeds += top_links


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


clearConsole()
	