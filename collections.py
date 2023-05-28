from collections import *

#TYPE 1: COUNTER

list = ['A','A','A','A','A','B','B','B','C','C','C','C',]

print(Counter(list))

#Counter can be called using: a) a list of items, b) a dictionary with keys and item counts, or c) keyword arguments matching names with item counts
#here, I just created a list and passed it; a list can also simply be made inside the parameter brackets
#output: Counter({'A': 5, 'C': 4, 'B': 3})

