# A neat little tool built into Pythons collection module
# 

from collections import Counter

# Counts the number of individual characters in a string
print(Counter('abracadabra'))

count = Counter('abracadabra')
print("a = ", count['a'], type(count))