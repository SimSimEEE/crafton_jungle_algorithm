N = int(input())
home = list(list(map(int,input().split())) for _ in range(N))
for i in range(1,N):
    for j in range(3):
        home[i][j] += min(home[i-1][j-1],home[i-1][j-2])
        
print(min(home[N-1]))