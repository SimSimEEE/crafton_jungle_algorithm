a, b = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

for i in range(a, b + 1):
    if i == 11:
        print(i)
        continue
    if len(str(i)) % 2 == 0:
        continue
    if palindrome(i):
        if is_prime(i):
            print(i)
print(-1)
