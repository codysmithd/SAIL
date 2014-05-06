
'''
Setup
'''

import os
import nltk
import ngram



# init assembler
#from sentence_assembler import sentence_assembler
#assembler = sentence_assembler()



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
		tagged_tokens = ngram.convertPos(tagged_tokens)

		# assemble sentence
		#print assembler.run(tagged_tokens)


clearConsole()
	