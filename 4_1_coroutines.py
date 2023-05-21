import time
from collections import deque


def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield


def printer():
    count = 1
    while True:
        if count % 3 == 0:
            print("Boom")
        count += 1
        yield


def main():
    while True:
        gen = queue.popleft()
        next(gen)
        queue.append(gen)
        time.sleep(1)


if __name__ == "__main__":
    queue = deque()
    queue.append(counter())
    queue.append(printer())
    main()
