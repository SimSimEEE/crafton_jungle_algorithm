def isPrime(n):
    if n == 1:
        return 1
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return 1 
        return 0
N = int(input())
numbers = list(map(int,input().split()))
for x in numbers:
    N -= isPrime(x)
print(N)