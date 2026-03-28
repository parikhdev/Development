'''Task 7 — Write an async context manager using async with'''
'''Write an async context manager db_connection() that:

Prints "Opening DB connection" on entry
Yields the string "db_session"
Prints "Closing DB connection" on exit

Then write a main() that:

Uses async with db_connection() as session
Prints "Using session: {session}"

Call it with asyncio.run().'''

from contextlib import asynccontextmanager
import asyncio
@asynccontextmanager
async def db_connection():
    print("Opening DB connection")
    yield "db_session"
    print("Closing DB connection")
async def main():
    async with db_connection() as session:
        print(f"using session: {session}")
asyncio.run(main())

'''When you are building modern, high-performance web backends—especially using frameworks like FastAPI—managing database connections is one of the most critical tasks.

Every time a user visits your website, your server needs to grab a connection to your MySQL database, get the data, and return it. But database connections are limited resources. If you forget to close a connection after a user's request is done, your server will eventually run out of connections and crash (a "connection leak").

Using @asynccontextmanager guarantees Resource Safety.

Even if your code crashes while fetching data inside the async with block (for example, if a table is missing or there's a typo in your SQL query), Python guarantees that it will still jump back up and run the code after the yield, ensuring your database connection is safely closed and returned to the pool.'''