import asyncio
import time


async def print_nums():
    num = 0
    while True:
        if num % 3 != 0:
            real_time_line = round(time.time() - cur_time, 2)
            print(f"TIME: {real_time_line} - {num} sec.")
        num += 1
        await asyncio.sleep(1)


async def print_modul():
    count = 0
    while True:
        if count % 3 == 0:
            real_time_line = round(time.time() - cur_time, 2)
            print(f"TIME: {real_time_line} - {count} PRINT!")
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_modul())
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    cur_time = time.time()
    asyncio.run(main())
