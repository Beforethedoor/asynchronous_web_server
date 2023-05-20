

def init_gen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print("StopIteration")
            break
        else:
            print("*"*10, message)
    return "return from subgen()"


@init_gen
def delegator(g):
    result = yield from g
    print(result)


sg = subgen()
dg = delegator(sg)
sg.send("OK")
sg.throw(StopIteration)
