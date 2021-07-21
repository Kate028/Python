Data Types


# Numeric
  ## Interger
  ## Complex Number
  ## Float

# Dictionary
# Boolean
# Set
# Sequence Type
  ## Strings
  ## List
  ## tuple


## Numeric
 Numeric value can be interger, floating number or even complex numbers. These values are defined as int, float and complex class in Python.

### Python program to demonstrate numeric value 
   
c = 1 + 1j
print("Type of a, b, and c is " , type(2), type(1.5), type(c) , "respectively")

output: Type of a, b, and c is  <class 'int'> <class 'float'> <class 'complex'> respectively

## Sequence
In Python, a sequence is the ordered collection of similar or different data types.

### String
### List
### Tuple

1) String: A string is a collection of one or more characters put in a single quote, double-quote or triple quote. In python there is no character data type, a character is a string of length one. It is represented by str class. Strings in Python can be created using single quotes or double quotes or even triple quotes.

## Python Program for Creation of String  
     
# String with single, double and triple quotes   
print('Welcome to the Python World', " I am a Pythonista", '''and I lives in world of "Python"''')

output: Welcome to the Python World  I am a Pythonista and I lives in world of "Python"

#### Python Program to Access characters of String  
String1 = "Pythonista"
     
#### Print First character 
print(String1[0])  
     
#### Print Last character 
print(String1[-1])  

## Deleting/Updating from a String –

In Python, Updation or deletion of characters from a String is not allowed because Strings are immutable. Only new strings can be reassigned to the same name.

## Python Program to Update / delete character of a String    
String1 = "Hello, I'm a Pythonista"
     
### Updating a character
String1[2] = 'a'
   
Output: TypeError: ‘str’ object does not support item assignment

### Deleting a character   
del String1[2]

Output: TypeError: ‘str’ object doesn’t support item deletion

# String Slicing in Python

Python slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end.
Python slicing can be done in two ways.

## slice() Constructor
## Extending Indexing

# String slicing  
String ='Pythonista'
  
# Using indexing sequence 
print(String[:3]) 
print(String[1:5:2]) 
print(String[-1:-12:-2]) 
  
# Prints string in reverse  
print("\nReverse String") 
print(String[::-1]) 

Output:
Pyt
yh
asnhy
Reverse String
atsinohtyP


Curious? okay please refer holybook of coding to know more
https://www.geeksforgeeks.org/string-slicing-in-python/


## List
Lists are just like the arrays, declared in other languages. A single list may contain DataTypes like Integers, Strings, as well as Objects. The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. It is represented by list class.

# Creating a List  
List = []  
print(List)  
     
# Creating a list of strings
List = ['Pythonista', 'Pythoneer'] 
print(List)  
     
# Creating a Multi-Dimensional List  
List = [['Python', 'For'], ['Beginners']]  
print(List)

Adding Elements to a List: Using append(), insert() and extend()

# Addition of elements in a List  
     
# Creating a List  
List = []
     
# Using append()
List.append(1)  
List.append(2)
print(List)  
   
# Using insert()
List.insert(3, 12)  
List.insert(0, 'Geeks')
print(List)  
   
# Using extend()  
List.extend([8, 'Geeks', 'Always'])  
print(List)

# accessing of element from list  
     
 
List = [1, 2, 3, 4, 5, 6]  
     
# accessing a element
print(List[0])   
print(List[2])  
   
# Negative indexing
# print the last element of list  
print(List[-1])
# print the third last element of list   
print(List[-3])
