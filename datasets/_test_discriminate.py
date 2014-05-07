'''
This file parses the Brown corpus, tags parts of speech, and puts out a JSON file for the corpus.
It takes a while...
'''

#locks to prevent accidental execution

import string



'''
Preprocess tokens
'''

remove = ["", "-", "--", "pa", "af", "u", "wb", "n't"]
containRemove = ["\"", "\'", "\'\'", ",", ":", "`", "``", "*", "@", "#", "/", "\\", "<", ">", "+", "=", "|", "_", "~", "^", "%", "&", "(", ")", "[", "]", "{", "}"]
fullstop = ["?", ";", "!", "!!", "!!!", "..", "...", "....", "'."]

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

# returns boolean of whether it should be added to the corpus
def discriminate(x):
	if x in remove: # predefined list of stuff to ditch
		return False
	if (x[0] == "u") and is_number(x[1:]): # no weird unicode characters
		return False
	if x[0] not in string.printable:
		return False
	for test in containRemove: # test if the string contains anything illegal
		if test in x:
			return False
	return True


while True:
	print discriminate(raw_input("Enter Word to discriminate: "))