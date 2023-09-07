def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weights = 0
    truck_weights.reverse()
    while truck_weights:
        answer += 1
        bridge_weights -= bridge.pop(0)
        if bridge_weights + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            bridge.append(truck)
            bridge_weights += truck
        else:
            bridge.append(0)

    return answer + bridge_length
