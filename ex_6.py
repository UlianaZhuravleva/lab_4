import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]


with open(path, encoding='utf8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(unique(field(arg,'job-name'),ignore_case = True), key = lambda x: x.upper())


@print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x.lower() and x[5].lower() == 'а' and x[7].lower() == 'м', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    b = map(lambda x: ', зарплата '+ str(x) + 'руб', gen_random(100000,200000,len(arg)))
    return list('{} {}'.format(c, d) for c,d in zip(arg,b))


with timer():
    f4(f3(f2(f1(data))))

