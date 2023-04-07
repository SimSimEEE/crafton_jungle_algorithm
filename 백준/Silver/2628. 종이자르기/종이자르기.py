import sys
input = sys.stdin.readline
x, y = map(int, input().split())
X = [0,x]
Y = [0,y]
for _ in range(int(input())):
    o, a = map(int, input().split())
    if o == 1:
        X.append(a)
    else:
        Y.append(a)
X.sort()
Y.sort()
width = 0
for i in range(1,len(X)):
    for j in range(1,len(Y)):
        width = max((X[i]-X[i-1])*(Y[j]-Y[j-1]),width)
print(width)