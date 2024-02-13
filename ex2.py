import asyncio
from random import randint
async def custom_sleep(task_id, timer):
    await asyncio.sleep(timer)
    print(f"{task_id} {timer } complete")

async def main():
    for i in range(10):
        task = asyncio.create_task(custom_sleep(i, randint(1, 10)))
        # task = asyncio.create_task(custom_sleep(i,10-i))
    # task1 = asyncio.create_task(custom_sleep(1,1))
    # task2 = asyncio.create_task(custom_sleep(2,2))
    await asyncio.sleep(11)
    print("finished")

asyncio.run(main())
# print(1)