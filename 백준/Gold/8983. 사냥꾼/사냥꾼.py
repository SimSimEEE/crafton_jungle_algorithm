import sys
input = sys.stdin.readline
M,N,L = map(int,input().split())
Mx = list(map(int,input().split()))
Nxy = [list(map(int,input().split())) for _ in range(N)]

hunted_animal = [False]*N

for i in range(N):
    if not hunted_animal[i]:
        for x in Mx:
            if Nxy[i][1]+Nxy[i][0] <= L + x and Nxy[i][1]-Nxy[i][0] <= L - x:
                hunted_animal[i] = 1

print(hunted_animal.count(1))