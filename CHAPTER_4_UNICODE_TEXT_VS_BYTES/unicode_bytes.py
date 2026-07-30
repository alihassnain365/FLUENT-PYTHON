"""1 . Exercise 1: String → Bytes"""

text = 'Ali Hassnain'

encoded_bytes = text.encode("utf-8")
print(encoded_bytes)
print(type(encoded_bytes))

del text
"""Exercise 2: Inspect Every Byte"""
text = "café"
text_byte = text.encode('utf-8')
print(text_byte)
print(text_byte[0])
print(text_byte[1])
print(text_byte[2])
print(text_byte[3])


