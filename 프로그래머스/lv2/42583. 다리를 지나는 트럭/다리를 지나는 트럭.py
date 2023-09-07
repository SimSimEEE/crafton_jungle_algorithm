def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weights = 0
    while truck_weights:
        answer += 1
        bridge_weights -= bridge.pop(0)
        if bridge_weights + truck_weights[0] <= weight :
            bridge.append(truck_weights.pop(0))
            bridge_weights += bridge[-1]
        else :
            bridge.append(0)

    return answer + len(bridge)