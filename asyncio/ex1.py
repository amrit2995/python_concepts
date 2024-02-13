import asyncio

async  def main():
    print("test")
    task = asyncio.create_task(foo('text'))
    # await asyncio.sleep(2)
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1) #asyncio.sleep(1) creates a couroutine and await runs it.

asyncio.run(main()) 