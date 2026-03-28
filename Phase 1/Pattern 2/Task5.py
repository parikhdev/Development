# Write an async function that calls an HTTP API (use httpx, not requests)
# www.python-httpx.org/async

'''Write an async function get_joke() that:

Calls this free API: https://official-joke-api.appspot.com/random_joke
Returns the setup and punchline fields from the response
Prints them nicely

Call it with asyncio.run().'''

import asyncio
import httpx

url = "https://official-joke-api.appspot.com/random_joke"
async def get_joke():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()
joke = asyncio.run(get_joke())
print(f"SetUp: {joke['setup']} \nPunchLine: {joke['punchline']}")