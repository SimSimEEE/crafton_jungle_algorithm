for _ in range(int(input())):
    n = int(input())
    tel_nums = list(input() for _ in range(n))
    tel_nums.sort(key=lambda x: [x, len(x)])
    answer = True
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tel_nums[i] in tel_nums[j]:
                if tel_nums[j].index(tel_nums[i]) == 0:
                    answer = False
                    break
            else:
                if tel_nums[i][0] != tel_nums[j][0]:
                    break
        if not answer:
            break
    if answer:
        print("YES")
    else:
        print("NO")
