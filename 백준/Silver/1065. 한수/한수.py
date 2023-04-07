import sys
input = sys.stdin.readline
n= int(input())
count = 0
if(n<100):
    print(n)
else:
    count = 99
    for i in range(100,n+1):   
         if(i//100+i%10==2*int(i//10%10)):
            count+=1
    print(count)