import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
products = deque(list(map(int, input().split())))

power_bar = []

cnt = 0
while products:
    if products[0] in power_bar:
        products.popleft()
        continue

    if len(power_bar) < N:
        power_bar.append(products.popleft())
        continue

    change_product, product_index = 0, 0
    for mounted_product in power_bar:
        if not mounted_product in products:
            change_product = mounted_product
            break
        elif products.index(mounted_product) > product_index:
            product_index = products.index(mounted_product)
            change_product = mounted_product
    power_bar[power_bar.index(change_product)] = products.popleft()
    cnt+=1

print(cnt)