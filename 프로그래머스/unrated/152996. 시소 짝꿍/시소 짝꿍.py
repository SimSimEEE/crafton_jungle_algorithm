from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    weight_values = list(counter.keys())
    G = [2, 3, 4]
    
    for i in range(len(weight_values)):
        for k in range(len(G) - 1):
            for j in range(k + 1, len(G)):
                if weight_values[i] * G[k] / G[j] in counter:
                    print(weight_values[i], weight_values[i] * G[k] // G[j])
                    answer += counter[weight_values[i]] * counter[weight_values[i] * G[k] // G[j]]
        answer += counter[weight_values[i]] * (counter[weight_values[i]] - 1) // 2
    
    return answer