N = int(input())
city_len = list(map(int,input().split()))
oil_price = list(map(int,input().split()))
min_price = oil_price[0]

result = 0
for i in range(N-1):
    min_price = min(oil_price[i], min_price)
    result += min_price * city_len[i]
    
print(result)