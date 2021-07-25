# Python Lists
# used to store multiple items in a single variable.
# created using square brackets
# List items are ordered(items have a defined order, and that order will not change.), 
# changeable(can change, add, and remove items in a list after it has been created.), 
# and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# If you add new items to a list, the new items will be placed at the end of the list.


iAmList = ["Katness", "Everdeen", "HungerGames"]
print(iAmList)

iAllowDuplicates = ["Katness", "Everdeen", "HungerGames", "Katness"]
print(iAllowDuplicates)

ListLength = ["Katness", "Everdeen", "HungerGames"]
print(len(ListLength))

# Data types: List items can be of any data type.
# String, int and boolean data types

  iAmListString= ["Katness", "Everdeen", "HungerGames"]
  iAmListInt = [1, 2, 10, 5, 3]
  iAmListBoolean = [True, False, False]

  print(iAmListString)
  print(iAmListInt)
  print(iAmListBoolean)

# A list with strings, integers and boolean values:
  DifferentDataTypes = ["kate" , 20, 10.0, True]
  print(DifferentDataTypes)
  print(type(DifferentDataTypes))

# The list() Constructor
# we can use the list() constructor for creating a new list.

  iAmConstructor = list(("Katness", "Everdeen", "HungerGames")) # use double round-brackets
  print(iAmConstructor)

# List Method
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

![image](https://user-images.githubusercontent.com/72349558/126911622-fa9031c0-11b4-455e-a6d6-db2f4cb94e2f.png)
