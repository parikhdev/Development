'''Write an async function greet(name) that:

Simulates a 1 second delay (like waiting for an API response)
Returns "Hello, {name}"

Call it with asyncio.run() and print the result.
Simple and quick — write it now.'''

import asyncio
async def greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}"
result = asyncio.run(greet("User1"))
print(result)
