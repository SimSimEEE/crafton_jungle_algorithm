for _ in range(int(input())):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = sorted(list(map(int,input().split())))
    cnt = 0
    for a in A:
        for b in B:
            if a > b:
                cnt+=1
            else:
                break
    print(cnt)