
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
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average


g = average()
print(g.send(None))
print(g.send(10))

try:
    g.throw(StopIteration)
except StopIteration as e:
    print(e.value)
