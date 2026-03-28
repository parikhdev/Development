'''Task 8 — Debug: identify why mixing sync code inside async breaks things'''
import asyncio 
import time

async def broken_code(name):
    print(f"The {name} Starts...")
    time.sleep(2) # sync code in async function
    #Fix is use: await asyncio.sleep(2)
    print(f"The {name } Done.")
async def main():
    await asyncio.gather(
        broken_code('A'),
        broken_code('B')
    )
start_time = time.perf_counter()
asyncio.run(main())
elapsed = (time.perf_counter() - start_time)
print(f"The time taken is: {elapsed:.2f} sec")