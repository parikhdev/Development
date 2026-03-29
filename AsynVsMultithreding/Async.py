import asyncio
import time

async def fetch_news_article_async(article_id):
    print(f"Task {article_id}: Starting to download...")
    # asyncio.sleep() is Non-blocking. 
    # It tells the Event Loop: "I'm waiting for 2 seconds. Go do something else!"
    await asyncio.sleep(2)
    print(f"Task {article_id}: Finished downloading!")
    return f"News Data {article_id}"

async def main_asyncio():
    start_time = time.time()
    
    # We create 3 tasks and hand them to our single "Super-Chef" (the Event Loop)
    tasks = [
        fetch_news_article_async(1),
        fetch_news_article_async(2),
        fetch_news_article_async(3)
    ]
    
    # Run them all concurrently
    await asyncio.gather(*tasks)
    
    print(f"\nAll articles fetched in {time.time() - start_time:.2f} seconds")

asyncio.run(main_asyncio())