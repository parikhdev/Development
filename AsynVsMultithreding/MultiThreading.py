import time
import concurrent.futures

def fetch_news_article(article_id):
    print(f"Thread {article_id}: Starting to download...")
    # time.sleep() simulates a blocking network request
    # It completely freezes this specific thread for 2 seconds
    time.sleep(2) 
    print(f"Thread {article_id}: Finished downloading!")
    return f"News Data {article_id}"

def main_threading():
    start_time = time.time()
    
    # We hire 3 (threads) 
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submiting the 3 tasks to the workers
        article_ids = [1, 2, 3]
        results = executor.map(fetch_news_article, article_ids)
        
    print(f"\nAll articles fetched in {time.time() - start_time:.2f} seconds")

main_threading()

'''
Older Method 

import threading

# 1. Create the threads
T1 = threading.Thread(target=fetch_news_article, args=(1,))
T2 = threading.Thread(target=fetch_news_article, args=(2,))
T3 = threading.Thread(target=fetch_news_article, args=(3,))

# 2. Tell the OS to start them
T1.start()
T2.start()
T3.start()

# 3. Tell main program to wait until they are finished
T1.join()
T2.join()
T3.join()
'''