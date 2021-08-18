"""Mab lib is one of the python projects for beginners.The input could be anything, an adjective, a noun, a pronoun, etc. 
Once all the inputs are entered, the application will take the data and arrange the inputs into a story template form."""

# concepts being used:
# string concatenation
# formatted output
# value = "Pythonista" # some string variable

# string formatting
# print("I am a " + value)
# print("I am a {}".format(value))
# print(f"I am a {value} ")

noun1 = input("What should I call you : ")
noun2 = input("Who is your friend: ")
adj = input("Give me an Adjective: ")
verb1 = input("and a Verb: ")
verb2 = input("one more Verb: ")

fav_hero = input("umm! Your Favorite Hero: ")

madlib = f"I am {noun1} and I am a Pythonista. Python is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Keep coding and {verb2} like you are {fav_hero}.{noun2} too like it and we both used to code all the time."
print(madlib)

# you can create as long story as you want!
