# generators are highly related to iterators
# first of all, an iterator is an object that allows you to loop through a sequence without having to store all of those items in memory
# a generator is a new type of syntax introduced in python 3 that allows you to create an iterator without having to go through the usual tedious process

import sys

# let's say we wanted to loop through the numbers 1 to 10

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list:
    print(i)

# this is a very simple and straightforward way to go about this problem; however, the issue is that it forces the computer to store the list in its memory
# this is not very efficient, and although it may be fine for small structures like this, it would be problematic with bigger ones

for i in range(1, 11):
    print(i)

# this is another simple solution, and it also eliminates the issue of storing the numbers in memory
# this is because the range function returns an iterator

y = map(lambda i: i**2, list) 

# the map function takes a data structure (in our case the list from above) and maps all of them to a function, in this case our lambda function 
# the thing about the map function is that it doesn't create a new list that contains all of those function calls; the map() function is actually a generator

# what a for loop really does is that it calls a special method on all of the iterator objects that gives us the next item in the sequence that we're looping through

print(next(y))
print(next(y))

for i in y:
    print(i) # starts at the third value because of the next() calls above

# what the for loop does is that it calls the next() function on an iterator object