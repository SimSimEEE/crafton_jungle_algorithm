import sys
input = sys.stdin.readline
s0 = ['m', 'o', 'o']
def sol(n, k, l):               
    new_l = 2*l + k + 3
    if n <= 3:                   
        print(s0[n-1])
        return
    if new_l < n:              
        sol(n, k+1, new_l)
    else:
        if n > l and n <= l+k+3:
            if n-l != 1:
                print('o')
            else:
                print('m')
            return
        else:
            sol(n-(l+k+3), 1, 3)
            
n = int(input())
sol(n, 1, 3)