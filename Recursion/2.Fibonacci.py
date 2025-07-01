# 🧪 Practice Problem 2:
# Write a recursive function to compute the nth Fibonacci number.


def fib(n):
    if n in [0, 1]:
        return n
    
    return fib(n - 1) + fib(n - 2)

print(fib(15))