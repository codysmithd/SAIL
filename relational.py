# Relational Node-based verb-noun graph
# Class used for creating, saving, modifying, and using graph of noun-verb probabilities

class relational:
	
	# Read State Constants
	SOURCE_WORD = 0
	NOUN_LIST = 1
	VERB_LIST = 2

	# Intialization method. Optionally takes filename to create from file
	def __init__(self, filename):
    	
    	self.filename = filename

    	self.nodeList = {} # Main node list

    	f = open(filename, 'w')

    	if(f):

    		read_state = SOURCE_WORD   # Current read-state
    		is_word = False            # Is the current item suppost to be a number

    		# For each line in the file
    		for line in f:
    			
    			if( read_state == SOURCE_WORD ):
    				
    				word = line.strip()

    				# Initialize list of list ([0] is noun, [1] is verb)
    				self.nodeList[word] = []
    				self.nodeList[word].append([])
    				self.nodeList[word].append([])
    				
    				read_state = NOUN_LIST

    			elif( read_state == NOUN_LIST ):
    				for word in line.split():
    					if(is_word):
    						self.nodeList[word][0].append(word)
    					else:
    						self.nodeList[word][0].append(int(word))
    					is_word = not is_word
    			
    			elif( read_state == VERB_LIST ):
    				for word in line.split():
    					if(is_word):
    						self.nodeList[word][1].append(word)
    					else:
    						self.nodeList[word][1].append(int(word))
    					is_word = not is_word
    		f.close()

    # Relates the lists of nouns and verbs to each other
    def addRelation(nouns, verbs):

    # Returns a list of assosiated words to input as a tuple with the weight
    def getWords(input_word):

    # Saves the relational to a text file
    def save(new_filename):
    	if(new_filename):
    		f = open(new_filename,'r')
    	else:
    		f = open(.filename)

