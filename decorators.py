# decorators allow you to change the behavior of a function without modifying the function itself
# a few uses of decorators: logging, testing performance, caching, and verifying permissions

# to understand decorators, it's important to know that a function is an object, and so the it can be assigned to and accessed through a variable

# def my_function():
#     print("I am a function.")

# description = my_function # when we assign a function to a variable, we don't use brackets, because that would execute the function

# print(description()) # prints out "I am a function"

# another thing to understand is that a function can be nested inside another function
# note that a function defined inside another function is not available outside the outer function

# def outer():
    
#     def inner():
#         print("I came from the inner function")

#     inner() # executes the inner function from the outer function

# outer()

# the third concept to understand is that, since a function can be nested inside another function, it can also be returned

# def outer():
#     task = "Read Python book chapter 3"

#     def inner():
#         print(task)

#     return inner

# homework = outer()

# homework()

# the last concept to understand is that a function can be passed to another function as a parameter of that function

# def reminder(func):

#     func()
#     print("Don\'t forget to bring your wallet!")

# def action():
#     print("I am going to the store to buy you something nice.")

# reminder(action)

# HOW TO CREATE A DECORATOR

from datetime import datetime


def log_datetime(func):
    # logs the date and time of a function

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime # the @ symbol tells python that this .daily_backup() function needs to be passed into .log_datetime()
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup() # when we run the .daily_backup() function, it doesn't run the function itself, but instead goes back to .log_datetime() and runs that function with .daily_backup() as its parameter