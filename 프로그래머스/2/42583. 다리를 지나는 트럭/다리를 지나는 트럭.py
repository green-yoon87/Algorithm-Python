from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    allWeight, time, fistTruckTime = 0, 0, 0
    truck_weights.reverse()
    gone = 0
    
    while gone < len(truck_weights): 
        time +=1 
        truck = truck_weights.pop()

        if bridge_length > len(bridge) and truck_weights:
            truck = bridge.append(truck_weights)
            if weight >= allWeight + int(truck):
                if bridge:
                    fistTruckTime = time
                bridge.append(truck_weights)
            else:
                truck_weights.append(truck)
        if (time -fistTruckTime)  == bridge_length:
            oneTruck = bridge.popleft()
            gone +=1
            allWeight -= goneTruck
            if bridge:
                firstTruckTime += 1
                
    return time
# bridge_length: 다리에 트럭이 최대로 올라갈 수 있는 수
# weight: 다리가 무게를 견딜 수 있는 무게 
# 모든 트럭이 다리를 건너려면 몇 초가 걸리는지 return
# bridge에 트럭이 들어갈 수 있고 트럭의 제한 무게는 제한해서 계산할 수 있는데
# 시간은 어떻게 할 것인가 - 예를 들어 시간이 경과함에 따라 트럭이 어떻게 다리를 지났는지 판단할 것인가 