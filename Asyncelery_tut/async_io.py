import asyncio


# Define a coroutine that simulates a time-consuming task
async def fech_data(delay: int, id: int):
    print(f"Fetching data... id: {id}")
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print(f"Data fetched... id: {id}")
    return {"data": "Some data", "id": id}  # Return some data


# # Define another coroutine that calls forst coroutine
# async def main():
#     print("Start of main coroutine")
#     task = fech_data(2)     # only create the object and do not await it
#     print("End of main coroutine")
#     # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
#     result = await task
#     print(f"Received result: {result}")

# # Define another coroutine that calls forst coroutine
# async def main():

#     task1 = fech_data(2, 1)     # only create the object and do not await it
#     task2 = fech_data(2, 2)     # only create the object and do not await it
    
#     # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
#     result1 = await task1
#     print(f"Received result: {result1}")

#     result2 = await task2
#     print(f"Received result: {result2}")


async def main():
    # Carete tasks for running coroutines concurrently
    task1 = asyncio.create_task(fech_data(1, 2))
    task2 = asyncio.create_task(fech_data(2, 3))
    task3 = asyncio.create_task(fech_data(3, 1))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)


# print(main())   # -> <coroutine object main at 0x0000022F630BCAC0>
asyncio.run(main())
