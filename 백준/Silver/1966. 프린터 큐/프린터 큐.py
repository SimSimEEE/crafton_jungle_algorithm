n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    lists = list(range(N))
    result = []
    for i in range(N):
        for _ in range(queue.index(max(queue))):
            queue.append(queue.pop(0))
            lists.append(lists.pop(0))
        queue.pop(0)
        result.append(lists.pop(0))
    print(result.index(M)+1)