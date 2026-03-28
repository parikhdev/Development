'''Write a decorator that takes arguments (@repeat(n=3))
peps.python.org/pep-0318'''

'''def outer(arg):            # takes the argument
    def decorator(func):   # receives the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # runs on every call
            # do something with arg
            return func(*args, **kwargs)
        return wrapper
    return decorator

@outer(arg=value)
def my_function():
    ...

**One gotcha:** You now have **3 levels** of nesting. The most common mistake is returning at the wrong level — accidentally returning `wrapper` from `outer` instead of returning `decorator`.


Write a `@repeat(n=3)` decorator that calls the wrapped function `n` times.
```
- outer function accepts n
- inner decorator wraps the function
- wrapper calls the function n times in a loop
- test it on a function that prints something simple'''

from functools import wraps

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapper       
    return decorator         

@repeat(n = 4)
def function(a,b):
    return a+b
x = function(2,3)
print(x)
            
            