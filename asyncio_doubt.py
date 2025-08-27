import asyncio

# First async function
async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(10)  # simulate IO work
    return {"data": 123}

# Second async function
async def process_data(data):
    print("Processing data...")
    await asyncio.sleep(1)  # simulate work
    return f"Processed: {data}"

async def process_data1(data):
    print("Processing data...1")
    # await asyncio.sleep(1)  # simulate work
    return f"Processed: {data}"

# Main async function calling the two
async def main():
    d = "Aman Singh"
    # data =  await fetch_data()      # Call first function
    # result = await process_data(data)  # Call second function
    # print(result)
    # result1 = await process_data1(d)
    # print(result1)

    # Schedule process_data1 to run concurrently
    t1 = asyncio.create_task(process_data1(d))

    # Collect the result of the concurrent task
    result1 = await t1
    print(result1)

    # Now await fetch_data; while it's sleeping, t1 can run
    data = await fetch_data()

    # Continue the dependent step
    result = await process_data(data)
    print(result)




# Run the async main
if __name__ == "__main__":
    asyncio.run(main())
