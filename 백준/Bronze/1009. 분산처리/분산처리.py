for _ in range(int(input())):
    a, b = map(int,input().split())
    a%=10
    b = b%4 + 4
    if a == 0:
        print(10)
    else:
        print(a**b%10)