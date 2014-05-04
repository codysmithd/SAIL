'''
File Format:
<SOURCE_WORD>
<NODE> <COUNT> ...
'''

# Class that contains a Word, Part Of Speech (POS), and of hash table of weighted sums to other words
class node:

    def __init__(self, word = "", pos = "", links = {}):
        self.word = word.lower()
        self.pos = pos.lower()
        self.links = links

    # Returns true if node is not null (empty)
    def __nonzero__(self):
        return self.word and self.pos 

    # Either adds weight to existing link or makes a new link
    def link(self, node, weight = 1):
        hash_index = node.word + " " + node.pos
        if(hash_index in self.links):
            self.links[hash_index] += 1
        else:
            self.links[hash_index] = weight

    # Returns a list of size n of the top links in-order, optionally given a Part Of Speech (POS)
    def get_top_links(self, n, pos = ""):
        top_links = []
        for key in self.links:
            if(key.split()[1] == pos or pos == ""):
                word = key.split()[0]
                value = self.links[key]
                if(len(top_links) > 1):
                    for x in xrange(0,len(top_links)):
                        if(value < top_links[x][1]):
                            top_links.insert(x,(word,value))
                else:
                    top_links.append( (word,value) )
        final_list = []
        for x in xrange(0,len(top_links)):
            if x < n:
                final_list.append(top_links[x][0])
            else:
                break
        return final_list

    # Returns a string formatted for output
    def print_out(self):
        buffer = "" + self.word + ' ' + self.pos + '\n'
        for key in self.links:
            buffer += key + ' ' + self.links[key] + ' '
        buffer += '\n'
        return buffer

    # Builds node based on string (assuming proper format)
    def read_in(self, string):
        lines = string.splitlines()
        self.word = lines[0].split()[0]
        self.pos = lines[0].split()[1]

        word = ""
        weight = 0
        links = lines[1].split()
        for x in xrange(0, len(links), 2)
            self.link(links[x],links[x+1])


# Class that contains a list of nodes that link to each other with weights.
class relational_map:

    def __init__(self):
        self.node_hash = {} # Note: Keys are given as "<word> <part_of_speech>""

    # Loads in a relational map from text file
    def load_from_file(self, filename):
        f = open(filename, 'r')
        if(f):
            lines = f.readlines()
            for x in xrange(0,len(lines),2):
                new_node = node()
                new_node.read_in(lines[x] + lines[x+1])
                node_hash[new_node.word + new_node.pos] = new_node
            f.close()

    # Outputs the relational map to a file with the given filename as text
    def output_file(self, filename):
        f = open(filename, 'w')
        if(f):
            for key in self.node_hash:
                f.write(self.node_hash[key].print_out())
            f.close()

    # Links the words. Words is a list of strings, formatted ["<word> <part_of_speech>", ... ]
    def link_words(self, words):
        
        [x.lower() for x in words]

        # Fix nodes not in node_hash
        for word in words:
            if(not word in self.node_hash):
                new_node = node(word.split()[0], word.split()[1])
                node_hash[word] = new_node

        # Link every word to every other word
        for x in xrange(len(words)):
            for y in words[0:x]:
                new_node



