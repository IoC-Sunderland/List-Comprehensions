# List Comprehension

# Example syntax:
# new_list = [expression for member in iterable]

names = ['gav', 'leo', 'ava'] 
names_capitalised = [name.upper() for name in names]
print(names_capitalised)

# Broken down

# names is the iterable
# name is the member
# name.upper() is the expression
# names_capitalised is the new_list

# Get Ascii codes of all chars in a string
ascii_codes = [ord(c) for c in list("capitalise me!")]
print(ascii_codes)

# Get the corresponding character for an ASCII code number
chars = [chr(c) for c in [70, 79, 85, 78, 68, 77, 69]]
print(chars)

