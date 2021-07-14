"""Below Python Programme demonstrate isnumeric
functions in a string"""
#Example:
s = '1242323'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

# s = '½'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s='python12'
print(s.isnumeric())

#Example 2: How to use isnumeric()?
#s = '²3455'
s = '\u00B23455'

if s.isnumeric() == True:
  print('All characters are numeric.')
else:
  print('All characters are not numeric.')
