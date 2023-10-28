n = int(input())
k = 15 * 10 ** 6
n %= k

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 1000000
    return a
print(fib(n))