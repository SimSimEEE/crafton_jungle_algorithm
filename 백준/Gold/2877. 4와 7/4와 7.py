k = int(input())
k = bin(k + 1)[3:]
print(k.replace('0', '4').replace('1', '7'))