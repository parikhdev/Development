'''Task 3: functools.wraps — understand why it matters
When you wrap a function with a decorator, Python replaces the original function with wrapper. That means the function loses its name, docstring, and metadata.
@wraps(func) copies that metadata back from the original function onto wrapper.
Real world use: debugging, logging, and API docs all rely on function names being correct. Without wraps, every decorated function shows up as wrapper in your logs.

Minimum Required Info
Imports:
from functools import wraps
Syntax pattern:
def decorator(func):
    @wraps(func)           # copies metadata from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
One gotcha: @wraps(func) goes on wrapper, not on decorator. People put it in the wrong place.

Your task:
Write two versions of a simple decorator — one without @wraps, one with it. On both, print:
pythonprint(function.__name__)
print(function.__doc__)'''

from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function of the decorator"""
        res = func(*args, **kwargs)
        print(res)
    return wrapper


@decorator
def my_function(a,b):
    """Adds two numbers"""
    return "Done"

my_function(2,3)

print(my_function.__name__)
print(my_function.__doc__)

# Without @wraps(function)

def dec(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper function of the decorator"""
        res = func(*args, **kwargs)
        print(res)
    return wrapper

@dec
def I_function(a,b):
    """Adds two numbers"""
    return "Done"

I_function(3,4)

print(I_function.__name__)
print(I_function.__doc__)

