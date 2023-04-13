import sys
input = sys.stdin.readline
N = int(input())
N_1 = N%10*10+(N//10+N)%10

def cicle(N_1,cnt):
    if N_1 == N:
        print(cnt)
        return
    cnt+=1
    cicle(N_1%10*10+(N_1//10+N_1)%10,cnt)

cicle(N_1,1)