from relational import relational_map

# Test relational_map

database = relational_map()

words = [("cow",1),("car",1),("king",1),("car",1),("blue",1),("land",1)]

database.link_words(words)

database.output_file("relational_test.txt")

print(database.get_top_links_for_word(("cow",1), 3 ) )

#database2 = relational_map()
#database2.load_from_file("relational_test.txt")

#database2.output_file("relational_test2.txt")