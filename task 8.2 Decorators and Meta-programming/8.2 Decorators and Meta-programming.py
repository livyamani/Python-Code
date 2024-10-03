import time
from functools import wraps


# Step 1: Custom decorators

# Decorator for logging function calls
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"I'm, calling {func.__name__} with these arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} gave back: {result}")
        return result
    return wrapper

# Decorator for timing function execution
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Decorator for access control (example with a simple check)
def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Simulate permission check
            if permission == "admin":
                return func(*args, **kwargs)
            else:
                raise PermissionError("Sorry, you don't have permission to access this.")
        return wrapper
    return decorator

# Step 2: Decorator to track function calls
def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


# Step 3: Simple metaclass to enforce constraints
class EnforceMethodsMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'required_method' not in attrs:
            raise TypeError(f"{name} needs to define a 'required_method'")
        return super().__new__(cls, name, bases, attrs)


# Step 4: Complex example with class registration
class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_class(cls, name):
        return cls.registry.get(name)


# Example usage of decorators

@logger
@timer
@call_counter
def sample_function(x, y):
    time.sleep(x)
    return x * 2, y * 2

@requires_permission('admin')
def admin_function():
    return "Admin access granted."

# Example class using the simple metaclass
class MyClass(metaclass=EnforceMethodsMeta):
    def required_method(self):
        print("This method is here and working.")

# Example class using the registry metaclass
class MyRegisteredClass(metaclass=RegistryMeta):
    pass

# Testing the functionality
if __name__ == "__main__":
    print("\n--- Testing sample_function ---")
    print(sample_function(1, 2))
    print(sample_function(2, 3))
    
    try:
        print("\n--- Testing admin_function without permission ---")
        print(admin_function())
    except PermissionError as e:
        print(e)

    print("\n--- Testing MyClass ---")
    my_instance = MyClass()
    my_instance.required_method()

    print("\n--- Registered Classes ---")
    print(RegistryMeta.registry)

    print("\n--- Getting a registered class by name ---")
    print(RegistryMeta.get_class("MyRegisteredClass"))
