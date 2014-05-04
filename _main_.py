
'''
Setup
'''

import nltk



# init relational
'''
from relational import relational_map
relational = relational_map()
'''

# init contextual_relational


# init assembler
from sentence_assembler import sentence_assembler
assembler = sentence_assembler()



'''
Main loop
'''

print "ready"

running = True
exit_words = ["done", "exit", "quit"]

while running:
	user_input = raw_input(">>> ").lower()

	if user_input in exit_words:
		running = False
	else:

		# tokenize
		tokens = nltk.word_tokenize(user_input)

		# filter for nouns and verbs
		tagged_tokens = nltk.pos_tag(tokens)
		print tagged_tokens

		# retreive relational words / update relations

		# assemble sentence

		# it all looks so easy when it's outlined like that ^

		print "\nGo away\n"
	