

class BlaBlasExceprion(Exception):
    pass


def init_gen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = "Ready to accept message"
    message = yield x
    print(message)


@init_gen
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlaBlasExceprion:
            print('BlaBlasExceprion')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average


g = average()
print(g.send(10))

try:
    g.throw(StopIteration)
except StopIteration as e:
    print(e.value)
