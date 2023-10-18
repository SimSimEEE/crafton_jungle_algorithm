n = int(input())
maps = {}
for _ in range(n):
    s, e = input().split(" is ")
    if s not in maps:
        maps[s] = e
    else:
        maps[s].append(e)
m = int(input())


def dfs(s, e):
    if s in maps:
        if e in maps[s]:
            return True
        else:
            for i in maps[s]:
                if dfs(i, e):
                    return True
    return False


for _ in range(m):
    s, e = input().split(" is ")
    if dfs(s, e):
        print("T")
    else:
        print("F")
