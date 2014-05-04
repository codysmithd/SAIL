from relational import relational_map

# Test relational_map

database = relational_map()

words = [("cow",1),("car",1),("king",1)]

database.link_words(words)

database.output_file("relational_test.txt")

for key in database.node_hash:
	print database.node_hash[key].word
	print database.node_hash[key].links