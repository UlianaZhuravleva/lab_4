import random


def field(items, *args):
    index = 0
    assert len(args) > 0
    if(len(args) == 1):
        for el in items:
            yield el.get(args[0])
            index += 1
    else:
        for el in items:
            d1 = {}
            for key in args:
                if (el.get(key) != None):
                    d1[key] = el[key]
                else:
                    break
            if (len(d1) != 0):
                yield d1


def gen_random(x,y,z):
    for i in range(z):
        yield random.randint(x, y)

