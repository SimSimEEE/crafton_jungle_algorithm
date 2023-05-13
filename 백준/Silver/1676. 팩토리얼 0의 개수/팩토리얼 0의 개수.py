n = int(input())

if n < 5:
    print(0)
    
else:
    num = 24
    zero_cnt = 0
    for i in range(5,n+1):
        num *= i
                    
    for s in str(num)[::-1]:
        if s == '0':
            zero_cnt += 1
        else:
            break
    print(zero_cnt)