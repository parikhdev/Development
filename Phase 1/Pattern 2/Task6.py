'''Task 6 — Understand when NOT to use async (CPU-bound vs IO-bound)'''

'''Explanation: Async can't help when the CPU is busy in processing then there is no waiting time to move to other tasks, It can only help with (Input/Outbut Bound Processes) i.e where waiting time is from external sources like Reading from PostgreSQL, Calling Groq api, Reading file from Disk...It can't help with (CPU Bound Processes) i.e where cpu is busy performing tasks like Processing PDFs, Training a Model, Matrix Multiplication etc '''

'''if you need to run CPU-bound work inside a FastAPI async endpoint without blocking the server, you can use:
pythonasyncio.get_event_loop().run_in_executor(None, your_cpu_function)
This offloads the CPU work to a thread pool so your async server doesn't freeze'''