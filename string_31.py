"""Below Python Programme demonstrate maketrans
functions in a string"""

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)
# translate string
print("Translated string:", string.translate(translation))
