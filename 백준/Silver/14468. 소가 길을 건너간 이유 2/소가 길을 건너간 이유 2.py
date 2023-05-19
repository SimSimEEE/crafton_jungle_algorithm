import sys

cow=list(sys.stdin.readline().rstrip())
alpha=[]
res=0
for i in cow:
	if i in alpha:
		res+=len(alpha)-alpha.index(i)-1
		alpha.remove(i)
	else:
		alpha.append(i)
print(res)