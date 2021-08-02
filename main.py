import operator
import time
from numba import jit
import numpy as np

arr = np.arange(3, 2500000)

@jit(nopython=True)
def iteratestuff(arr):
    for i in arr:
        initial = i
        maxval = i
        localmin = i
        localmax = i
        while i != 1:
            # if we get any lower than the number we started with, then we have already checked that number
            if i<initial:
                break
            # if the number is even, divide it by 2,
            if operator.imod(i, 2) == 0:
                i = i/2
                # if we have reached the same local min, then we are in a loop!
                if i==localmin:
                    return i
                # if this isnt a repeat local min, save this one (as we have divided and our min has gone down)
                localmax = i
            else:
                i=(i*3)+1
                # if we have multiplied back up to an already seen max val, then we are in a loop!
                if i == maxval or i == localmax:
                    return i
                localmin = i
                maxval = max(maxval, i)
    return -1


# records the time it takes to check the numbers
start=time.time()
print(iteratestuff(arr))
end = time.time()

print("Elapsed = %s" % (end - start))
