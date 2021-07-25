# slicing operations for a string.

a = "Hello"
print(a)
print("a[1] = " , a[1])  # e

print("a[-2] = ", a[-2])  # l

print("a + 'world' = ", a+"world") # Helloworld

print("a[1:] = " , a[1:])  # ello

print("a[1:4:2] = ", a[1:4:2]) # el

print("a[2:4] = ",a[2:4])   # ll

print("a[:] = ",a[:])    # Hello

print("a[::] = ",a[::])   # Hello

print("a[::1] = ",a[::1]) # Hello

print(a[::-1])    # olleH

print(a[::-3])   # oe

print(a[4:4:1])   # nothing

print(a[-1:-5:-1])  # olle

print(a[-5:-1:1])   # Hell

print(a[-5:])    # Hello

print(a[::-2])  # olH

print(a[::-1])  # olleH


# string functions - lower(),upper(),capitalise(),find(),index(),replace()

# The functions upper() and lower() returns the string by converting all 
# the characters of the string to upper case or lower case respectively.

string1 = "I AM PYTHONISTA."
print(string1.lower())  # lower() doesn't take any parameter

string2 = "i love data science."
print(string2.upper())  # upper() doesn't take any parameter

string3 = "i am an open source enthusiast."
print(string3.capitalize())  #converts the first character of the string to a capital

# The find() method finds the first occurrence of the specified value.
# Syntax = string.find(value, start, end)
text = "Hey folks, I am Kritika Ranjan"
weAreFinding = text.find("Kritika")

print(weAreFinding)

# The index() method returns the position at the first occurrence of the specified value.
# string.index(value, start, end)

text1 = "I like contributing to open source software"
weAreFindingIndex = text1.index("c",20,35)
print(weAreFindingIndex)

# The replace() method replaces a specified phrase with another specified phrase.
text2 = "I love Playing"
replacing = text2.replace("Playing" , "Chess")
print(replacing)

# use of format() function with placeholder on a string.

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# Syntax: string.format(value1, value2...)
text3 = "I am {age} year old".format("age", age = 23)
print(text3)