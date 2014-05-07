
'''
Setup
'''

import os
import nltk
import structures
import sentence_assembler


# inits
structures.load()
sentence_assembler.load()



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

		# choose a structure
		struct = structures.getRandom()

		# assemble sentence
		#print sentence_assembler.rateSentence(tagged_tokens)
		print sentence_assembler.run([0, 1], tagged_tokens)


clearConsole()
	