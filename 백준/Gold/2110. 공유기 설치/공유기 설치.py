import sys
input = sys.stdin.readline
n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])
start, end = 1, houses[n-1] - houses[0]
result = 0

if c == 2:
    print(houses[n-1] - houses[0])
else:
    while start<end:
        count = 1
        mid = (start+end)//2
        visited_house = houses[0]
        for house in houses:
            if house-visited_house>=mid:
                count+=1
                visited_house = house
        if count < c:
            end = mid
        else:
            result = mid
            start = mid+1
    print(result)