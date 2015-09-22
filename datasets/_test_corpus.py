
import json


'''
Load corpus
'''

print("loading JSON corpus...")

# load the tagged corpus
f = open("tagged_corpus.json", 'r')
if(f):
	sentences = json.load(f)
else:
	print("no corpus file")
	input() # hold for user
f.close()


while True:
	print(sentences[int(input("Enter Number of Sentence: "))])
