
import ngram

ngram.load()

while True:
	print ngram.queryBackward(raw_input("Enter word to test: "))
