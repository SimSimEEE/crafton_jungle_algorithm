def solution(stones, k):
    answer = max(stones)
    min_jump = min(stones)
    while answer >= min_jump:
        zero_num = 0
        jump = (answer + min_jump) // 2
        for stone in stones:
            if jump >= stone:
                zero_num += 1
            else:
                zero_num = 0
            if zero_num >= k:
                break
        if zero_num >= k:
            answer = jump - 1
        else:
            min_jump = jump + 1
    return answer + 1