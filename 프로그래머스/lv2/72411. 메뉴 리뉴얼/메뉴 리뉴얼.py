from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course:
        maps = {}
        max_count = 0
        for order in orders:
            nCr = list(combinations(order, num))
            for c in nCr:
                c = ''.join(sorted(c))  # Sort the combination for consistency
                if c not in maps:
                    maps[c] = 1
                else:
                    maps[c] += 1
                max_count = max(max_count, maps[c])

        for key, value in maps.items():
            if value == max_count and value > 1:
                answer.append(key)

    return sorted(answer)
