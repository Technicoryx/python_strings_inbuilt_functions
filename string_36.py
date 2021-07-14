
text = "Python is easy to learn."
result = text.startswith('is easy')

# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)

# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)

# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('program', 7, 18)
print(result)

#startswith() With Tuple Prefix
text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)
result = text.startswith(('is', 'easy', 'java'))
# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)
