from collections import deque


def gen1(s):
    for i in s:
        yield i
        print(f"gen1 foo after {i}")


def gen2(n):
    for i in range(n):
        yield i
        print(f"gen2 foo after {i}")


g1 = gen1("asdf")
g2 = gen2(4)
tasks = deque([g1, g2])


while tasks:
    task = tasks.popleft()

    try:
        i = next(task)
        print(i)  # it can be something usefull
        tasks.append(task)
    except StopIteration:
        pass
