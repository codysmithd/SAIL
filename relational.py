# Relational Node-based verb-noun graph
# Class used for creating, saving, modifying, and using graph of noun-verb probabilities

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

    def __nonzero__(self):
        return self.word and self.pos 

    def link(self, node, weight = 1):
        if(node.word in self.links):
            self.links[node.word] += 1
        else:
            self.links[node] = weight

    def print_out(self):
        buffer = "" + self.word + ' ' + self.pos + '\n'
        for key in self.links:
            buffer += key + ' ' + self.links + ' '
        buffer += '\n'
        return buffer

    def read_in(self, string):
        lines = string.splitlines()
        self.word = lines[0].split()[0]
        self.pos = lines[0].split()[1]

        word = ""
        weight = 0
        links = lines[1].split()
        for x in xrange(0, len(links), 2)
            self.link(links[x],links[x+1])


# Class that contains a list of nodes that link to each other with weights
class relational_map:

	def __init__(self):
        self.node_list = {}

    def load_from_file(self, filename):
        f = open(filename, 'r')
        if(f):
            lines = f.readlines()
            for x in xrange(0,len(lines),2):
                new_node = node()
                new_node.read_in(lines[x] + lines[x+1])
                node_list[new_node.word] = new_node
            f.close()

    def output_file(self, filename):
        f = open(filename, 'w')
        if(f):
            for key in self.node_list:
                f.write(self.node_list[key].print_out())
            f.close()
