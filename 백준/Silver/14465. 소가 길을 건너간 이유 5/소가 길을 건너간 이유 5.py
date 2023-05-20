N, K, B = map(int, input().split())
lights = [0]*N

for _ in range(B):
    lights[int(input())-1] = 1

result = K
fix = sum(lights[0:K])
for i in range(0, N-K):
    fix = fix - lights[i]+lights[i+K]
    result = min(result, fix)

print(result)