import time
import math

def timing_decorator(func):
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken in: {func.__name__}: {end - begin:.4f} seconds")
        return result
    return inner

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned: {result}')
        return result
    return wrapper

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 1: After function call")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 2: After function call")
        return result
    return wrapper

# parameterized decorator
def decorator(like):
    print("Inside decorator")
    
    def inner(func):
        print("Inside inner function")
        print("I like", like) 
        def wrapper():
            func()
        return wrapper
    return inner

# Parameterized decorator to repeat function n times
def repeat(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i+1} of {n}")
                func(*args, **kwargs)
        return wrapper
    return inner

print("Time decorator and Logger decorator\n")
@timing_decorator
@logger_decorator
def factorial(num):
    time.sleep(2)
    return math.factorial(num)

print("Factorial Function Calls:")
factorial(10)
factorial(20)

print("\nMultiple decorator")
@decorator1
@decorator2
def add(a, b):
    return a + b

print("\nAdd Function Call:")
result = add(2, 3)
print("Result:", result)

print("\nParametarized decorator\n")
@decorator(like="geeksforgeeks")
def my_func():
    print("Inside actual function")

my_func()

print("\nParametarized decorator to repeat a function `n` times")
@repeat(3)
def greet():
    print("Hello!")

print("\nRepeated Function Calls:")
greet()