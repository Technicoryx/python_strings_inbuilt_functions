"""Below Python Programme demonstrate ljust
functions in a string"""

#Example:
# example string
string = 'cat'
width = 5

# print right justified string
print(string.rjust(width))

#Right justify string and fill the remaining spaces
# example string
string = 'cat'
width = 5
fillchar = '*'

# print right justified string
print(string.rjust(width, fillchar))
