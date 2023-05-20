import asyncio
from time import time

import aiohttp

URL = "https://loremflickr.com/320/240/paris,girl/all"
COUNT_PICTURE_TO_DOWNLOAD = 10


# bad practice (use sync code with async)
def write_image(data):
    file_name = f"file_{int(time() * 1000)}.jpeg"
    with open(file_name, "wb") as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url=url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data=data)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(COUNT_PICTURE_TO_DOWNLOAD):
            task = asyncio.create_task(fetch_content(url=URL, session=session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    time_start = time()
    asyncio.run(main())
    print(time() - time_start)
