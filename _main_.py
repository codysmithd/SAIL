
'''
Setup
'''

import nltk

# init relational
# init contextual_relational
# init assembler



'''
Main loop
'''

running = True

while running:
	user_input = raw_input(">>> ").lower()

	if user_input == "done" or user_input == "exit":
		running = False

	# tokenize
	tokens = nltk.word_tokenize(user_input)
	print "tokens: " + tokens

	# filter for nouns and verbs
	#tagged_tokens = nltk.pos_tag(tokens)
	#print "tagged_tokens: " + tagged_tokens

	# retreive relational words / update relations

	# assemble sentence

	# it all looks so easy when it's outlined like that ^

	print "\nGo away\n"
	