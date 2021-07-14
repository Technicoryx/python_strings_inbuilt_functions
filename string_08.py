"""Below Python Programme demonstrate expandtabs
functions in a string"""

#Case1 : With no Argument
str = 'xyz\t12345\tabc'
# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)

#Case 2:Different Argument
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))



