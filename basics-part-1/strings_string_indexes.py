# String Slicing
numbered_string = '01234567'

# [start]
# [start:stop]
# [start:stop:stepover]
print(numbered_string[0]) # prints character at the index of 0
print(numbered_string[0:7]) # print characters starting at index of 0 and stop before index of 7
print(numbered_string[2:5]) # start at index of 2 and stop before index of 5
print(numbered_string[1:]) # start at index of 1 and go to the end 
print(numbered_string[:5]) # start at the beginning and stop before index of 5
print(numbered_string[::1]) # start at the beginning and go to the end
print(numbered_string[-1]) # start at the end of the string (e.g. 7)
print(numbered_string[-3]) # start at the end of the string and grab the character at index of 3 (e.g. 5)
print(numbered_string[::-1]) # reverses the string