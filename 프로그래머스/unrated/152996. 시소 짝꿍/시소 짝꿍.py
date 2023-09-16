from collections import Counter
def solution(weights):
    answer = 0
    weight_counter = Counter(weights)
    unique_weights = list(weight_counter.keys())
    ratios = [2, 3, 4]
    for i in range(len(unique_weights)):
        for k in range(len(ratios) - 1):
            for j in range(k + 1, len(ratios)):
                ratio = unique_weights[i] * ratios[k] / ratios[j]
                if ratio in weight_counter:
                    print(unique_weights[i], ratio)
                    answer += weight_counter[unique_weights[i]] * weight_counter[ratio]
        answer += weight_counter[unique_weights[i]] * (weight_counter[unique_weights[i]] - 1) // 2
    return answer
