n = int(input())
dough_price, topping_price = map(int, input().split())
dough_cal = int(input())
topping_cal = [int(input()) for _ in range(n)]
topping_cal.sort(reverse=True)

total_price = dough_price
total_cal = dough_cal
total_ratio = total_cal / total_price
i = 0

while i < n and (total_cal + topping_cal[i]) / (total_price + topping_price) >= total_cal / total_price:
    total_cal += topping_cal[i]
    total_price += topping_price
    i += 1
    total_ratio = total_cal / total_price

print(int(total_ratio))
