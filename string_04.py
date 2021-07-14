"""Below Python Programme demonstrate casefold
functions in a string"""

string = "PYTHON IS AWESOME"
# print lowercase string
print("Lowercase string:", string.casefold())
firstString = "der Fluß"
secondString = "der Fluss"

# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
