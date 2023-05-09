
#3
def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n], cache
    return wrapper
@cache_decorator
def fibonacci(n):
    if n in(0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))