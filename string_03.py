"""Below Python Programme demonstrate split
functions in a string"""
text= 'Love thy neighbor'
# splits at space
print(text.split())
grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.split(', '))
# Splitting at ':'
print(grocery.split(':'))

#How split() works when maxsplit is specified
grocery = 'Milk, Chicken, Bread, Butter'
# maxsplit: 2
print(grocery.split(', ', 2))
# maxsplit: 1
print(grocery.split(', ', 1))
# maxsplit: 5
print(grocery.split(', ', 5))
# maxsplit: 0
print(grocery.split(', ', 0))




