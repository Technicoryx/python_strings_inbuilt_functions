"""Below Python Programme demonstrate islower
functions in a string"""
#Example:
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

#Example2:

s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')

s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
