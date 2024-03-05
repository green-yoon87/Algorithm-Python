from collections import deque
def solution(bridge_length, weight, truck_weights):
    time, allWeight = 0, 0
    bridge = deque([])
    truck_weights.reverse()
    
    while bridge or truck_weights:
        time += 1
        if bridge:
            if time -bridge[0][1] >= bridge_length:
                element = bridge.popleft()
                allWeight -= element[0]
                
        if truck_weights:
            truck = truck_weights[-1]
            if len(bridge) < bridge_length and truck + allWeight <= weight:  #트럭을 다리에 추가할 수 있는 상황
                bridge.append((truck, time))
                allWeight += truck 
                truck_weights.pop()
    return time