
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
	print("Please install NLTK, with pyYAML and numpy")
	sys.exit()

try:
	nltk.pos_tag(["asdf", "asdf"])
except:
	print("NLTK requires maxent_treebank_pos_tagger to continue.")
	print("In the python console, run the following:")
	print(">>> import nltk")
	print(">>> nltk.download()")
	sys.exit()


# inits
structures.load()
sentence_assembler.load()

print("Creating short term memory...")
short_term = short_term_relational()

print("Loading long term memory...")
try:
	long_term = relational_map()
	long_term.load_from_file("long_term.pickle")
except:
	print("No long-term memory!")
	print("Please generate it by running _generate_longterm.py")
	sys.exit()


def clearConsole():
	os.system(['clear','cls'][os.name == 'nt'])

clearConsole()



'''
Main loop
'''

running = True
exit_words = ["done", "exit", "quit", "exit()"]
remove_chars = [".", "," ,"\"", "\'", "!", "?", ";", "`", "~", "@", "#", "$", "%", "^", "&", "*", "=", "+", "-", "_", "(", ")"]

while running:
	user_input = input(">>> ").lower()

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
		user_keywords = []
		primary_words = []
		secondary_words = []

		for token in tagged_tokens:

			# get the top links for this token
			top_links = long_term.get_top_links_for_word(token, 50)
			top_links += short_term.get_top_links_for_word(token, 50)

			# sort the new words based on part-of-speech priority
			if token[1] in primary_pos_tags:
				primary_words += top_links
				primary_words.append(token)
				user_keywords.append(token) # save off a list of the users nouns and verbs
			else:
				secondary_words += top_links
				secondary_words.append(token)


		result = ""
		count = 20
		while (result == "") and (count > 0):
			struct = structures.getRandom()
			#print "choose structure: " + str(struct)
			result = sentence_assembler.run(struct, user_keywords, primary_words, secondary_words)
			count -= 1

		if result == "":
			print("I'm sorry user, I'm afraid I can't respond to that...")
		else:
			print("\n" + str(result[0]) + "\n")

		# Ask if this result makes sense TODO


clearConsole()
