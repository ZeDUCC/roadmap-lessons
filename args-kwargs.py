# *args are non-keyword arguments
# **kwargs are keyword arguments
# we use these when we are unsure of how many arguments to pass to a function

# *ARGS EXAMPLE

def adder(*num):
    sum = 0
    
    for n in num:
        sum += n

    print(sum)

adder(3, 5)
adder(3, 5, 93)
adder(3, 5, 93, 13)

# **KWARGS EXAMPLE

def introduction(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value)) # substitutes curly brackets with each key and value in that order

introduction(first_name = "Janahan", last_name = "Sivaneswaran", age = 18, city = "Toronto")