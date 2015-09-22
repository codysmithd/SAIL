
import ngram

ngram.load()

while True:
	user_input = input("Enter word to test: ")
	print(ngram.get_unigram_score("<s>", user_input))
