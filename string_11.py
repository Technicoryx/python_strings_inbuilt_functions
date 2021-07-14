"""Below Python Programme demonstrate format
functions in a string"""

#Substring argument Only
sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)

result = sentence.index('Java')
print("Substring 'Java':", result)

sentence = 'Python programming is fun.'
# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))
# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))
# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))
