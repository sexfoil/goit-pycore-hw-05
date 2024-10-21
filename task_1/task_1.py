def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if cache.get(n):
            return cache.get(n)
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci



fib = caching_fibonacci()

print(fib(10))  # Result must be 55
print(fib(15))  # Result must be 610
