'''
File Format:
<SOURCE_WORD>
<NODE> <COUNT> ...
'''

# Class that contains a Word, Part Of Speech (POS), and of hash table of weighted sums to other words
class node:

    #TODO
    def __init__(self, word = "", pos = ""):
        self.word = word.lower()
        self.pos = pos.lower()
        self.links = {}
        self.hash_index = self.word + " " + self.pos

    # Returns true if node is not null (empty)
    def __nonzero__(self):
        return self.word and self.pos 

    # Either adds weight to existing link or makes a new link
    def link(self, node_word, node_pos, weight = 1):

        hash_index = node_word + " " + node_pos

        if(hash_index != self.hash_index):
            if(hash_index in self.links):
                self.links[hash_index] += weight
            else:
                self.links[hash_index] = weight

    # Returns a list of size n of the top links in-order, optionally given a Part Of Speech (POS)
    def get_top_links(self, n, pos = ""):
        top_links = []
        for key in self.links:
            if(key.split()[1] == pos or pos == ""):
                top_links.append( (key.split()[0], self.links[key]) )
        top_links.sort(key=lambda tup: tup[1], reverse=True) 
        return [ value[0] for value in top_links[:n] ]

    # Returns a string formatted for output
    def print_out(self):
        buffer = "" + self.word + ' ' + self.pos + '\n'
        for key in self.links:
            buffer += key.replace(' ','_') + ' ' + str(self.links[key]) + ' '
        buffer += '\n\n'
        return buffer

    # Builds node based on string (assuming proper format)
    def read_in(self, string):
        lines = string.splitlines()

        # First line: "<word>  <part_of_speech>"
        self.word = lines[0].split()[0]
        self.pos = lines[0].split()[1]

        # 2nd line: "<word>_<part_of_speech> <weight>"
        links = lines[1].split()
        for x in xrange(0, len(links), 2):
            node = links[x].split('_')
            self.link(node[0],node[1],links[x+1])


# Class that contains a list of nodes that link to each other with weights.
class relational_map:

    def __init__(self):
        self.node_hash = {} # Note: Keys are given as "<word> <part_of_speech>""

    # Loads in a relational map from text file
    def load_from_file(self, filename):
        f = open(filename, 'r')
        if(f):
            lines = f.readlines()
            for x in xrange(0,len(lines),3):
                new_node = node()
                new_node.read_in(lines[x] + lines[x+1])
                self.node_hash[new_node.word + new_node.pos] = new_node
            f.close()

    # Outputs the relational map to a file with the given filename as text
    def output_file(self, filename):
        f = open(filename, 'w')
        if(f):
            for key in self.node_hash:
                f.write(self.node_hash[key].print_out())
            f.close()

    # Links the words. Words is a list of tuples, formatted [(<word>,<part_of_speech>), ... ]
    def link_words(self, words_tuple):
        
        # convert words_tuple in words (where words[n] = "<word> <part_of_speech>")
        words = []

        for word_tuple in words_tuple:
            words.append(word_tuple[0] + " " + str(word_tuple[1]))

        # Add nodes not in node_hash
        for word_index in words:
            if(not word_index in self.node_hash):
                w = word_index.split()
                new_node = node(w[0], w[1])
                self.node_hash[word_index] = new_node

        # Link every word to every other word
        for x in xrange(len(words)):

            current_word = words[x]

            # If this is not the first occurance of this word, skip this cycle
            if(words.count(current_word) > 1 and words.index(current_word) != x):
                continue

            # words before
            for word in words[:x]:
                split_word = word.split()
                self.node_hash[current_word].link( split_word[0], split_word[1])

            # words after
            for word in words[x+1:]:
                split_word = word.split()
                self.node_hash[current_word].link( split_word[0], split_word[1])

    # Returns a list of the top links given a word_tuple (<word>, <part_of_speech>), as a list of tuples [(word, pos), ...]
    def get_top_links_for_word(self, word_tuple, n, pos = ""):
        # make "<word> <part_of_speech>" for indexing hash
        word_index = word_tuple[0] + " " + str(word_tuple[1]);
        if word_index in self.node_hash:
            return self.node_hash[word_index].get_top_links(n,pos)
        else:
            raise Exception("Word tuple: " + str(word_tuple) + " not in network")