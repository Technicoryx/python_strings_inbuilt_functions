"""Below Python Programme demonstrate find
functions in a string"""

quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if  (quote.find('be,') != -1):
  print("Contains substring 'be,'")
else:
  print("Doesn't contain substring")

#start and end Arguments

quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))
# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))
# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))


