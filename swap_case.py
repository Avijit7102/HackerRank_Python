"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

# swapcase() is a built in string method in python.
# we can do solve this problem using swapcase()
#########################################################

s = input("Enter your string: ")
res = s.swapcase()
print(res)

# another method
result = []
for letter in s:
    if letter.isupper():
        result.append(letter.lower())
    elif letter.islower():
        result.append(letter.upper())
    else:
        result.append(letter)

r = ''.join(result)
#  The join() method concatenates all char elements into a single string, with '' (an empty string) as the separator.
print(r)