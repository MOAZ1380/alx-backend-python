# 0-basic_async_syntax.py
# '''Asyncronos Python'''
# import asyncio
# import random
# import time
# from typing import List






## 1--

# wait_random = __import__('0-basic_async_syntax').wait_random



import asyncio
import random
import time
from typing import List

def task_wait_random( max_delay: int):
    return  asyncio.create_task(wait_random(max_delay))

async def wait_random(max_delay: int = 10) -> float:
    '''an asynchronous coroutine'''
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return a list of awaited response from previous function'''
    lis = []
    for i in range(n):
        ma = await wait_random(max_delay)
        lis.append(ma)
    return sorted(lis)

async def wait_n(n: int, max_delay: int) -> List[float]:
    lis = []
    for i in range(n):
        ma = await wait_random(max_delay)
        lis.append(ma)
    return sorted(lis)

# def measure_time(n: int, max_delay: int) -> float:
#     start = time.time()
#     asyncio.run(wait_n(n, max_delay))
#     return (time.time() - start) / n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))


# async def wait_random(max_delay: int = 10)->float:
#     '''an asynchronous coroutine'''
#     wait = random.uniform(0, max_delay)
#     await asyncio.sleep(wait)
#     return wait

# async def wait_n(n: int, max_delay: int) -> List[float]:
#     lis = []
#     for i in range(n):
#         ma = await wait_random(max_delay)
#         lis.append(ma)
#     return sorted(lis)

# def measure_time(n: int, max_delay: int) -> float:
#     start = time.time()
#     asyncio.run(wait_n(n, max_delay))
#     return (time.time() - start) / n


# n = 5
# max_delay = 9

# print(measure_time(n, max_delay))





# import random

# # Generate a random float between 1 and 10
# # Generate a random float between -5 and 5
# # Generate a random float between 1 and 10 with two decimal places
# random_number = round(random.uniform(1, 10), 2)
# print(random_number)






# import asyncio
# import random

# async def producer(queue):
#     for i in range(5):
#         item = random.randint(1, 10)
#         await queue.put(item)
#         print(f"Produced {item}")
#         await asyncio.sleep(1)

# async def consumer(queue):
#     while True:
#         item = await queue.get()
#         print(f"Consumed {item}")
#         queue.task_done()

# async def main():
#     queue = asyncio.Queue()
#     await asyncio.gather(producer(queue), consumer(queue))

# asyncio.run(main())




# import asyncio

# async def task1():
#     print("Task 1: Start")
#     await asyncio.sleep(2)
#     print("Task 1: End")

# async def task2():
#     print("Task 2: Start")
#     await asyncio.sleep(2)
#     print("Task 2: End")

# async def main():
#     # Run both tasks concurrently
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())



# import asyncio

# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(1)  # Simulate a non-blocking I/O operation
#     print("World")

# # To run the coroutine
# asyncio.run(say_hello())




# import asyncio
# import time

# async def fetch_data(delay):
#     print(f"Fetching data with a delay of {delay} seconds...")
#     await asyncio.sleep(delay)  # Simulate an I/O-bound operation
#     return f"Data fetched after {delay} seconds"

# async def main():
#     tasks = [
#         fetch_data(2),
#         fetch_data(3),
#         fetch_data(1)
#     ]
#     results = await asyncio.gather(*tasks)  # Run tasks concurrently
#     for result in results:
#         print(result)

# # Run the main function in the event loop
# asyncio.run(main())

# #!/usr/bin/python3
# '''Coding challenge.
# '''


# def minOperations(n):
#     '''Computes the fewest number of operations needed to result '''
#     count = 0
#     while(n > 1):
#         if (n % 3 == 0):
#             n //=3
#             count+=3
#         elif (n % 2 == 0):
#             n //= 2
#             count+=2
#         else:
#             count+=n
#             n = 1
            
#     return count
            




# for i in range(1, 11):
#     print(f"Min # of operations to reach {i} chars: {minOperations(i)}")


# def minimum_operations(num : int) -> int:
#     count : int = 0
#     while(num > 1):
#         if (num % 3 == 0):
#             num //=3
#             count+=1
#         elif(num % 2 == 0):
#             num//=2
#             count+=1
#         else:
#             num-=1
#             count+=1
#     return count +2
            


# print(minimum_operations(12))  # لا حاجة لأي عملية
# print(minimum_operations(2)) # 1 → 2 (عملية واحدة)
# print(minimum_operations(3))   # 1 → 3 (عملية واحدة)
# print(minimum_operations(4))  # 1 → 2 → 4 (عمليتان)
# print(minimum_operations(5)) # 1 → 2 → 4 → 5 (ثلاث عمليات)
# print(minimum_operations(10)) # 1 → 2 → 4 → 5 → 10 (أربع عمليات)
# print(minimum_operations(15)) # 1 → 3 → 4 → 8 → 9 → 15 (خمس عمليات)
# print(minimum_operations(7) )# 1 → 2 → 3 → 6 → 7 (أربع عمليات)
# print(minimum_operations(50))# 1 → 2 → 4 → 5 → 10 → 11 → 50 (ست عمليات)





