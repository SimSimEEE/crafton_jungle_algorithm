from itertools import permutations

def sieve_eratosthenes(n):
    sieve = set(range(2, n))
    for i in range(2, int(n ** 0.5) + 1):
        if i in sieve:
            sieve.difference_update(range(i * i, n, i))
    return sieve

k, m = map(int, input().split())
result = 0
pri_set = sieve_eratosthenes(10 ** k)

for i in permutations(range(10), k):
    if i[0] == 0:
        continue
    n = int(''.join(map(str, i)))
    is_prime = False
    for j in pri_set:
        if n - j in pri_set and n - j != j:
            is_prime = True
            break
    a = n
    while a % m == 0:
        a //= m
    for j in pri_set:
        if a % j == 0 and a // j in pri_set and is_prime:
            result += 1
            break

print(result)