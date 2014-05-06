import json


# load the tagged corpus
f = open("tagged_corpus.json", 'r')
if(f):
	sentences = json.load(f)
else:
	print "no corpus file"
	raw_input() # hold for user
f.close()



for sentence in sentences:
        for word in sentence:
                try:
                        v = word[1]
                except:
                        print word
