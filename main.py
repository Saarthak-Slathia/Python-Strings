# print('This is Chapter-2 on Strings')

# Accessing String Elements
# String Elements are accessed from 0
# Example: 
 
msg = "Hello"
a = msg[0] # Will store H
b = msg[1] # Will store e
c = msg[2] # Will store l
d = msg[3] # Will store l
e = msg[4] # Will store o
print(a, b, c, d, e)
print(msg)

# Slicing a substring

print(msg[2:4]) # Does not include the last index value, .: it will print ll 
 

# String Properties
# All strings are of built-in type str
 
# Example: 
msg = "Hello World"
typeof = type(msg)

print(typeof) # Return <class = "str">
 
# Python strings are immutable or cannot be changed.
 
# Two Strings can be concatinated using + symbol.
msg1 = "Hello "
msg2 = "World"
msg = msg1 + msg2
print(msg) # Yields Hello World.
 
# Replication Strings
 
way1 = '*'*50
print(way1)
 
# Condition checking in strings
 
msg = 'Hello'
print('e' in msg) # Yields True as e is there in Hello
print('s' in msg) # Yields False as s is not there in Hello
 

# String Operations
    # Syntax: string.name_of_function()

    # Content Test functions
        # isalpha() --> Checks if all characters are alphabets
        # isdigit() --> Checks if all characters are numbers
        # isalnum() --> Checks if all characters are of type complex or contains both alphabets and digits
        # islower() --> Checks if all characters are in lower-case
        # isupper() --> Checks if all characters are in uppper-case
        # startswith() --> Checks if all characters starts with a value
        # endswith() --> Checks if all characters ends with a value

    # Conversions
        # lower() --> Converts the string into lower-case.
        # upper() --> Converts the string into upper-case.
        # capitalize() --> Converts first character of the string into upper-case.
        # swapcase() --> Swaps cases in the string.

    # Find and Replace
        # find() --> Searches for it's value, returns the position
        # replace() --> Relpaces one value with the other

    # Other Functions
        # lstrip() --> Trims the string from the left.
        # rstrip() --> Trims the string from the right.
        # split() --> Splits the string at a specified seperator string.
        # partition() --> Partitions the string into 3 parts at first occurence of specified string.
        # str() --> Returns a numeric string for its numeric argument.
        # chr() --> Returns a string representing its Unicode value.
        # ord() --> Returns a Unicode Value representing its string.