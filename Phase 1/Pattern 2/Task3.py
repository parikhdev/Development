'''Write an async function fetch_data(source) that:

Prints "{source} fetching..."
Waits 2 seconds
Returns "{source} done"

Then write a main() that:

Runs fetch_data("OpenAI") and fetch_data("Database") concurrently using gather()
Stores the results
Prints the results list

Call main() with asyncio.run() and measure total time — it should be ~2 seconds not ~4.'''

import asyncio
import time
async def fetch_data(source):
    print(f"{source} fetching...")
    await asyncio.sleep(2)
    return f"{source} done"
start = time.time()
async def main():
    results = await asyncio.gather(
        fetch_data("OpenAI"),
        fetch_data("Database")
    )
    return results
res = asyncio.run(main())
print(res)
print(f"Time taken is: {time.time() - start}")