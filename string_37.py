
#Example:
text = 'My favorite number is 25.'
print(text.title())

text = '234 k3l2 *43 fun'
print(text.title())

#Example 3: Using Regex to Title Case String
import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),
     s)

text = "He's an engineer, isn't he?"
print(titlecase(text))

