from relational import relational_map

# Test relational_map

database = relational_map()

print("Loading in database")

database.load_from_file("long_term.pickle")

print("database loaded")

while(True):
	user_input = input("\nWhat would you like to see links for?\n")
	print(("Top links for " + user_input.split()[0]))
	print((database.get_top_links_for_word((user_input.split()[0],1), 50) ))
