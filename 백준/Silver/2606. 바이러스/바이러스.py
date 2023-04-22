from collections import deque
n=int(input())
s=int(input())
bfs = [0]*(n+1)
nets=[[] for _ in range(n+1)]
for _ in range(s):
    x,y = map(int,input().split())
    nets[x].append(y)
    nets[y].append(x)
bfs[1] = 1
dq=deque([1])
while dq:
    d = dq.popleft()
    for net in nets[d]:
        if bfs[net] == 0:
            dq.append(net)
            bfs[net] = 1
print(sum(bfs)-1)