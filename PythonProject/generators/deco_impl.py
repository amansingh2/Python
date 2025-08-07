def nirala(pr):
    def wrapper(*args , **kwargs):  #yehi structure follow karna padega , pattern yehi rahega naam kuchh bhi likh sakte hai!
        for _ in range(5):
            pr(*args)
    return wrapper





@nirala
def add(x , y , z):
    print(x , y , z)

add(4 , 5 , 0)


import asyncio

# async def hello():
#     print("Hello")
#     await asyncio.sleep(10)  # Simulates an I/O operation
#     print("World")
#
# asyncio.run(hello())  # Runs the event loop
#


# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)  # Simulating an I/O-bound task
#     print("Data received")
#
# asyncio.run(fetch_data())



async def task_1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task_2():
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    t1 = asyncio.create_task(task_1())  # Start Task 1
    t2 = asyncio.create_task(task_2())  # Start Task 2
    await t1  # Wait for Task 1 to finish
    await t2  # Wait for Task 2 to finish

asyncio.run(main())