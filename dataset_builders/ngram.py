
import pickle

from nltk.corpus import brown
from nltk.probability import LidstoneProbDist
from nltk.model.ngram import NgramModel

print "building model..."

estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
model = NgramModel(2, brown.words(), True, False, estimator)

print "model built..."


print "pickling..."

# dump the model
f = open("ngram_model.p", 'w')
pickle.dump(model, f)
f.close()

print "enjoy your pickle"
raw_input() # freeze screen when done
