import time
from collections import deque


def counter():
    count = 1
    while True:
        if count % 3 != 0:
            real_time_line = round(time.time() - cur_time, 2) + 1
            print(f"TIME: {real_time_line} - {count} sec.")
        count += 1
        yield


def printer():
    count = 1
    while True:
        if count % 3 == 0:
            real_time_line = round(time.time() - cur_time, 2) + 1
            print(f"TIME: {real_time_line} - {count} rocket start!")
        count += 1
        yield


def main():
    while True:
        gen = queue.popleft()
        next(gen)
        queue.append(gen)
        time.sleep(0.5)


if __name__ == "__main__":
    cur_time = time.time()
    queue = deque()
    queue.append(counter())
    queue.append(printer())
    main()
