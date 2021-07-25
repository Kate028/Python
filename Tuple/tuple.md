#### Tuples are used to store multiple items in a single variable.
#### 4 built-in data types for storing collection of data.
#### Tuple # list # set # dictionary

#### ordered(have a defined order, and that order will not change.) and unchangeable(cannot change, add or remove items after the tuple has been created.),(immutable), round brackets, allow duplicate values.
\n
iAmtuple = ("Katness" , "Everdeen", "HungerGames")
print(iAmtuple)

iAllowDuplicates = ("Katness" , "Everdeen", "HungerGames", "Katness" )
print(iAllowDuplicates)
print(len(iAllowDuplicates))  # len() func determine no of items in tuple

#### To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tupleWithOneItem = ("kate",)
print(tupleWithOneItem)
print(type(tupleWithOneItem))

#### String, int and boolean data types
iAmTupleString = ("Katness" , "Everdeen", "HungerGames")
iAmTupleInt = (1, 2, 10, 5, 3)
iAmTupleBoolean = (True, False, True)

print(iAmTupleString)
print(iAmTupleInt)
print(iAmTupleBoolean)

#### A tuple can contain different data types

iCanContain = ("kate", 40, True, 10.0)
print(iCanContain)

#### tuple() Constructor # Using the tuple() method to make a tuple
tupleConstructor = tuple(("I", "am", "Pythonista"))
print(tupleConstructor)

![image](https://user-images.githubusercontent.com/72349558/126910551-f7f28131-3f88-4d0b-a1c5-f9a9b5504797.png)
