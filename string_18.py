"""Below Python Programme demonstrate isprintable
functions in a string"""
#Example:
s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())


#Example2:

# written using ASCII
# chr(27) is escape character
# char(97) is letter 'a'

s = chr(27) + chr(97)
if s.isprintable() == True:
  print('Printable')
else:
  print('Not Printable')

  s = '2+2 = 4'
if s.isprintable() == True:
  print('Printable')
else:
  print('Not Printable')

