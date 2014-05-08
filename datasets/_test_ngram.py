
import ngram

ngram.load()

while True:
	user_input = raw_input("Enter word to test: ")
	user_input = user_input.split(" ")
	print ngram.rateSentence(user_input)
