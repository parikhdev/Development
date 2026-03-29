import asyncio
import concurrent.futures
import time

# Our simulated heavy task (e.g., passing an image through a neural network)
def heavy_ml_inference(image_name):
    time.sleep(3) # Simulates 3 seconds of heavy CPU blocking work
    return f"[{image_name}] Done!"

# Approach 1: The Slow, Synchronous Way 
def run_synchronously():
    print("--- Running Synchronously (One by One) ---")
    start_time = time.time()
    
    # Task 1 starts, takes 3 seconds, finishes.
    heavy_ml_inference("cat_photo.jpg")
    # Task 2 starts, takes 3 seconds, finishes.
    heavy_ml_inference("dog_photo.jpg")
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Synchronous Time: {total_time:.2f} seconds\n")
    return total_time

# Approach 2: The Fast, Concurrent Way (Asyncio + Threads) 
async def run_concurrently():
    print("--- Running Concurrently (Asyncio + Threads) ---")
    start_time = time.time()
    
    loop = asyncio.get_running_loop()
    
    # We open a pool with 2 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        # Start Both tasks at the exact same time
        task1 = loop.run_in_executor(pool, heavy_ml_inference, "cat_photo.jpg")
        task2 = loop.run_in_executor(pool, heavy_ml_inference, "dog_photo.jpg")
        
        # Await them both together
        await asyncio.gather(task1, task2)
        
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Concurrent Time: {total_time:.2f} seconds\n")
    return total_time

# --- The Final Showdown ---
async def main():
    sync_time = run_synchronously()
    async_time = await run_concurrently()
    
    time_saved = sync_time - async_time
    print(f"🔥 Total Time Saved: {time_saved:.2f} seconds!")
    print(f"⚡ Speed Increase: {((sync_time / async_time)/2) * 100:.0f}% faster.")


asyncio.run(main())