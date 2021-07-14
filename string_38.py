text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))

#How zfill() works with Sign Prefix?
number = "-290"
print(number.zfill(8))

number = "+290"
print(number.zfill(8))

text = "--random+text"
print(text.zfill(20))
