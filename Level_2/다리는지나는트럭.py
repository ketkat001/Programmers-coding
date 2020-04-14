def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    bridge_time = []
    time, idx = 0, 0
    while True:
        temp_idx = 0
        for i in range(len(bridge_time)):
            bridge_time[i] -= 1
            if bridge_time[i] == 0:
                temp_idx = i + 1
        bridge_time = bridge_time[temp_idx:]
        in_bridge = in_bridge[temp_idx:]
        if idx < len(truck_weights):
            next_truck = truck_weights[idx]
            if sum(in_bridge) + next_truck <= weight:
                in_bridge.append(next_truck)
                bridge_time.append(bridge_length)
                idx += 1
        if not in_bridge:
            break
        time += 1
    answer = time + 1
    return answer


print(solution(2, 10, [7, 4, 5, 6]))