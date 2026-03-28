import time
import asyncio
def our_function(name):
    print(name + "start")
    time.sleep(2)
    print(name + "done")
start1 = time.time()
def i_function():
    our_function("User1 ")
    our_function("User2 ")
    return 'done'
i_function()
print(f" The Sync time is: {time.time() - start1}")

async def all_function(name):
    print(name + " start")
    await asyncio.sleep(2) 
    print(name + " done") 
start2 = time.time()
async def my_function():
    await asyncio.gather(
        all_function("User3"),
        all_function("User4")
    )
    return 'done'
asyncio.run(my_function())
print(f" The Async time is: {time.time() - start2}")