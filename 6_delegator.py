
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


def delegator(g):
    result = yield from g
    print(result)


sg = subgen()
dg = delegator(sg)
sg.send(None)
sg.send("OK")
sg.throw(StopIteration)
