'''Task 1 — Write a decorator from scratch'''
'''A decorator is a function that wraps another function to add behavior before or after it runs — without modifying the original function.
Real world use: @app.get("/users") in FastAPI is a decorator — it registers a function as a route handler without you having to do it manually.'''


'''Write a decorator log_call that prints "Calling: {function name}" before the function runs
Then prints "Done" after it runs
Apply it to a function add(a, b) that returns a + b
Print the result

The function name is available via func.__name__.
'''
from functools import wraps

def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling: {function.__name__}")
        result = function(*args, **kwargs)
        print(result)
        print("Done")
        return result
    return wrapper

@log_call
def add(a,b):
    return a+b
res = add(5,5)

# print(dir(wraps)) checking the functions available in the wraps module