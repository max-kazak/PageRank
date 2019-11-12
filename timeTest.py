import time
# a = {i: i for i in xrange(100000000)}
# b = [i for i in xrange(100000000)]
t = time.time()
for x in xrange(0, 100000):
    a = x ** 10000
# for x in xrange(0, 100000000):
#     b[x]
print time.time() - t
