import time, sys

def fibonacci(n, cache={}):
    print(n, cache)
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)

n = int(sys.argv[1])

start = time.time()
print(fibonacci(n))
end = time.time()
print("Time taken: {} ms".format((end - start) * 1000))

start = time.time()
print(fibonacci2(n))
end = time.time()
print("Time taken: {} ms".format((end - start) * 1000))
