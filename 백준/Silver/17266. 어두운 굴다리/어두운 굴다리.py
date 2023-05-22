n = int(input())
m = int(input())
lights = list(map(int, input().split()))

height = max(lights[0], n - lights[-1])
for i in range(1, m):
    diff = lights[i] - lights[i - 1]
    height = max(height, (diff + 1) // 2) 

print(max(height, lights[0], n - lights[-1])) 