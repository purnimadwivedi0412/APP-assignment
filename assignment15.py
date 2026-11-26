import gc
import time


gc.enable()

print("Initial Garbage:", gc.get_count())


class Demo:
    def __init__(self):
        self.ref = self

objects = [Demo() for _ in range(100000)]

del objects


print("Before Collection:", gc.get_count())


start = time.time()
collected = gc.collect()
end = time.time()

print("Objects Collected:", collected)
print("Collection Time:", end - start)
print("After Collection:", gc.get_count())
'''
Output:
Initial Garbage: (602, 3, 0)
Before Collection: (557, 5, 4)
Objects Collected: 100000
Collection Time: 0.016261577606201172
After Collection: (2, 0, 0)
'''