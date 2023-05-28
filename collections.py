from collections import *

#TYPE 1: COUNTER

list = ['A','A','A','A','A','B','B','B','C','C','C','C',]

print(Counter(list))

#Counter can be called using: a) a list of items, b) a dictionary with keys and item counts, or c) keyword arguments matching names with item counts
#here, I just created a list and passed it; a list can also simply be made inside the parameter brackets
#output: Counter({'A': 5, 'C': 4, 'B': 3})

#TYPE 2: ORDERED_DICT

od = OrderedDict()
od['A'] = 1
od['B'] = 2
od['C'] = 3
od['D'] = 4
od.pop('A') #takes out the A key from the dictionary
od['A'] = 5 #adds a new A key to the end of the dictionary

for key, value in od.items(): #OrderedDict items need to be printed using the .items() method; this gives an array of tuples with a key and a value in each
    print(key, value)

#an OrderedDict works like a regular Dictionary; the only difference is that it keeps track of the order in which each key-value pair was added
#so, the A that I popped and re-added in lines 20-21 was taken out and then appended to the end of the dictionary, rather than bringing it back to the front, where it was originally

#TYPE 3: DEFAULT_DICT

d = defaultdict(int) #initializes a DefaultDict object that will be filled with only variables of the int type

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
    d[i] += 1

print(d)

#not really sure what this container is for, will come back later once fully understood

#TYPE 4: CHAIN_MAP

d1 = {'A': 1, 'B': 2, 'C': 3}
d2 = {'D': 4, 'E': 5, 'F': 6}
d3 = {'G': 7, 'H': 8, 'I': 9}

c = ChainMap(d1, d2, d3)

d4 = {'J': 10}

print(c)

chain2 = c.new_child(d4)

print(chain2)

#ChainMap combines two or more dictionary into a dictionary of dictionaries
#its functionality is practically the same as a normal dictionary; you can call keys and values just like you normally would
#the .new_child() function creates a new ChainMap using the one it's called on, adding to the beginning the dictionary passed in as a parameter