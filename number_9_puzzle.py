# using the numbers 1-9 inclusive, make:
# _ _ _ _ * 3 = _ _ _ _ _

import random

n = range(1,10)

q = []
a = []

while True:
    random.shuffle(n)
    q = int(''.join(str(x) for x in n[0:4]))
    a = int(''.join(str(x) for x in n[4:9]))

    if q*3 == a:
        print q, a
        break
