from relational import relational_map
import cPickle as pickle

# Test relational_map

database = relational_map()

print("Loading in database")

#with open("relational_pickle.data",'wb') as file_pointer:
 #   database = pickle.load(file_pointer)

database.load_from_file("output.txt")

print("database loaded")

# Add cow to db
database.link_words(
		[
			("cow",1),
			("cheese",1)
		]
	)

print(database.get_top_links_for_word(("cow",1), 5 ) )