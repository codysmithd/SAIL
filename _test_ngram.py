
import ngram

ngram.load()

while True:
	user_input = raw_input("Enter word to test: ")
	print ngram.get_unigram_score("<s>", user_input)
