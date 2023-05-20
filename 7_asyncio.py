import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_modul():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} moduled by 3!")
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_modul())
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())
