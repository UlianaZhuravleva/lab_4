from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'aaa', 'Aaa', 'aAa']
data2 = gen_random(1, 3, 10)

for i in Unique(data1):
    print(i)

print()

for i in Unique(data2):
    print(i)