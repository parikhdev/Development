'''Task 5: Generator functions using yield — explain how it differs from return
A generator produces values one at a time instead of building the whole list in memory. Critical when processing large datasets — like streaming 10,000 document chunks through a RAG pipeline without loading everything at once.

Minimum Required Info
Imports: None.
Syntax pattern:
pythondef my_generator():
    yield value1
    yield value2

gen = my_generator()
next(gen)   # gets value1
next(gen)   # gets value2
One gotcha: A generator is lazy — it doesn't run until you ask for the next value. Calling my_generator() does nothing by itself.

Your task:
Write a generator function that yields numbers 1 to n. Then:

Call it with next() three times manually
Loop through it with a for loop
Answer this: what happens if you call next() after the generator is exhausted?'''

def generator(n):
    num = 0
    while num <= n:
        yield num
        num += 1
    
for i in generator(5):
    print(i)