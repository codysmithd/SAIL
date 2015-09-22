from relational_short_term import short_term_relational
import nltk

short_term = short_term_relational()

while True:
	user_input = input("\nEnter a sentance:\n")
	tokens = nltk.word_tokenize(user_input)
	tagged_tokens = nltk.pos_tag(tokens)
	short_term.link_words(tagged_tokens)
	print(tagged_tokens)
