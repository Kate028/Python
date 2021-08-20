# Tuples are used to store multiple items in a single variable.
# 4 built-in data types for storing collection of data.
# Tuple # list # set # dictionary

# ordered(have a defined order, and that order will not change.) and unchangeable(cannot change, add or remove items after the tuple has been created.),(immutable), round brackets, allow duplicate values.

# I can be Empty   # output ()
empty_tuple = ()
print(empty_tuple)

# A tuple with string
iAmtuple = ("Katness" , "Everdeen", "HungerGames")
print(iAmtuple)

# I can be String, int and boolean data types
iAmTupleString = ("Katness" , "Everdeen", "HungerGames")
iAmTupleInt = (1, 2, 10, 5, 3)
iAmTupleBoolean = (True, False, True)

print(iAmTupleString)
print(iAmTupleInt)
print(iAmTupleBoolean)

# I allow Duplicates
iAllowDuplicates = ("Katness" , "Everdeen", "HungerGames", "Katness" )
print(iAllowDuplicates)
print(len(iAllowDuplicates))  # len() func determine no of items in tuple

tuple1 = ("katness")
print(type(tuple1))   # <class 'str'>

# To create tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tupleWithOneItem = ("kate",)
print(tupleWithOneItem)
print(type(tupleWithOneItem))

# without Parenthesis
tuple_p = "katness",
print(type(tuple_p))

# I can contain mixed data types as well
iCanContain = ("kate", 40, True, 10.0)
print(iCanContain)

# nested tuple
nested_tuple = ("katness", [3,4,5], (6,7,8))
print(nested_tuple)

# tuple() Constructor # Using the tuple() method to make a tuple
tupleConstructor = tuple(("I", "am", "Pythonista"))
print(tupleConstructor)

# I can be created without using parentheses (tuple packing).
tuple_packing = "katness", 5, 3
print(tuple_packing)

# tuple unpacking
a, b, c = tuple_packing
print(a ,b ,c)

# accessing tuple elements using indexing
tuple_indexing = ('t', 'u', 'p', 'l', 'e')
print(tuple_indexing[0])  # t
print(tuple_indexing[4])  # e
print(tuple[6])   # IndexError: list index out of range

# nested index
n_tuple = ("katness", [2,5,8],(4,3,1))

print(n_tuple[0][3])  # n
print(n_tuple[2][1])  # 3

# index must be an integer
print(tuple_indexing[2.0])
