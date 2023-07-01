N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i)))+i==N:
        ans = i
        break
print(ans)