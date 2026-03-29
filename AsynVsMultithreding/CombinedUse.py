import asyncio
import concurrent.futures
import time

# 1. This is a standard, OLD-SCHOOL blocking function.
# It does NOT use async/await. It uses the blocking time.sleep().
# If run directly in an async loop, it would crash the concurrency.
def heavy_ml_inference(image_name):
    print(f"[{image_name}] Thread starting heavy CPU work...")
    time.sleep(3) # Simulating a 3-second blocking operation
    return f"[{image_name}] ML prediction complete!"

async def main():
    # Get the current Asyncio Super-Thread
    loop = asyncio.get_running_loop()
    
    print("Event Loop: Running fast async tasks...")
    
    # Create our "back room" of worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        
        print("Event Loop: Uh oh, a heavy ML task came in. Delegating it to the pool...")
        
        # We tell the Event Loop to throw the heavy function into the ThreadPool.
        # It returns an awaitable task!
        task1 = loop.run_in_executor(pool, heavy_ml_inference, "cat_photo.jpg")
        task2 = loop.run_in_executor(pool, heavy_ml_inference, "dog_photo.jpg")
        
        # While the threads are doing the heavy lifting, the Event Loop is FREE
        # to do other things here if it wanted to!
        
        # Now we await the results from the threads just like normal async tasks
        results = await asyncio.gather(task1, task2)
        
        print(f"Event Loop: Got the results back from the threads! {results}")


asyncio.run(main())