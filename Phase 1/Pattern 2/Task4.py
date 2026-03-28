'''Explain Coroutines, async and await'''

'''1. Coroutines

In standard Python, a function (a subroutine) runs from top to bottom. Once you call it, it owns the thread until it returns.

A coroutine is a more generalized function. It can suspend its execution before reaching return, save its current state (local variables, execution line), and pass control back to the caller. Later, it can be resumed right where it left off. Under the hood in Python, coroutines are built on top of generators.

2. async and await (The Syntax)
These are the keywords used to write coroutines and manage their execution.

async def: You use this to define a coroutine.

Crucial detail: Calling an async def function does not execute it. Instead, it returns a coroutine object. To actually run it, you must pass it to the Event Loop.

await: This keyword can only be used inside an async def function. It marks a suspension point. When Python hits an await something(), it yields control of the thread back to the Event Loop until something() is finished.

3. asyncio (The Event Loop)

asyncio is Python's standard library for writing concurrent code. Its beating heart is the Event Loop.

The Event Loop is essentially an infinite while loop that manages a queue of tasks.

It looks at the queue and picks up Task A.

Task A runs until it hits an await (e.g., waiting for a database response over the network).

Task A yields control. The Event Loop says, "Okay, Task A is blocked. What's next?"

It picks up Task B and runs it.

When the database finally responds to Task A, the Event Loop flags Task A as "ready." When Task B yields or finishes, the loop resumes Task A.'''

import asyncio
import time

# 1. 'async def' creates a coroutine
async def fetch_data(id, delay):
    print(f"Task {id}: Requesting data...")
    # 2. 'await' tells the event loop to pause this task and go do something else
    await asyncio.sleep(delay) # Simulating a network request
    print(f"Task {id}: Data received!")

async def main():
    start_time = time.time()
    
    # We schedule both coroutines to run concurrently on the event loop
    task1 = asyncio.create_task(fetch_data(1, 2)) # Takes 2 seconds
    task2 = asyncio.create_task(fetch_data(2, 3)) # Takes 3 seconds
    
    # Wait for both to finish
    await task1
    await task2
    
    print(f"Total time: {time.time() - start_time:.2f} seconds")

# 3. 'asyncio.run' starts the Event Loop
asyncio.run(main())