from relational import relational_map
from relational import node

# Short-term relational database that 'decrements' each link based on when it was added
class short_term_relational(relational_map):

    def __init__(self):
       relational_map.__init__(self)
       self.time = 0       # Global 'time' as an int value of number of accesses
       self.time_deg = 100 # Value global time gets divided by to increase weights (larger = less steep curve)

    def link_words(self, words_tuple):
        
        self.time += 1

        weight = 1 + self.time/self.time_deg

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
                self.node_hash[current_word].link( split_word[0], split_word[1], weight)

            # words after
            for word in words[x+1:]:
                split_word = word.split()
                self.node_hash[current_word].link( split_word[0], split_word[1], weight)