# Python Sets: used to store multiple items in a single variable.
# unordered and unindexed, written with curly brackets.
# Sets are unordered(the items in a set do not have a defined order), so you cannot be sure in which order the items will appear.
# Set items are unchangeable(we cannot change the items after the set has been created), and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed: Sets cannot have two items with the same value.

iAmSet = {"Katness", "Everdeen", "HungerGames"}
print(iAmSet)

iDontLikeDuplicates = {"Katness", "Everdeen", "HungerGames", "Katness"}
print(iDontLikeDuplicates)

lengthOfSet = {"I", "am", "a Pythonista"}
print(len(lengthOfSet))

# Data Types: Set items can be of any data type

iAmSetString= ["Katness", "Everdeen", "HungerGames"]
iAmSetInt = [1, 2, 10, 5, 3]
iAmSetBoolean = [True, False, False]

print(iAmSetString)
print(iAmSetInt)
print(iAmSetBoolean)

DifferentDataTypes = ["kate" , 20, 10.0, True]
print(DifferentDataTypes)
print(type(DifferentDataTypes))

# Using the set() constructor to make a set
iAmConstructor = set(("Katness", "Everdeen", "HungerGames")) # use double round-brackets
print(iAmConstructor)   
![image](https://user-images.githubusercontent.com/72349558/126912042-c003c509-2af5-4570-a85e-b8c6221c92dc.png)
