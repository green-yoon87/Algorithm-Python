def solution(cap, n, deliveries, pickups):
    answer = maxDistance =  0 
    d = p = n-1
    
    while d >=0 or p >=0:
        while deliveries[d] == 0 and d >= 0:
            d -=1
        while pickups[p] == 0 and  p >= 0:
            p -=1
        maxDistance = max(d, p) +1
        deliverSum = pickupSum = 0
        
        while d >=0 and deliverSum < cap:
            if deliverSum + deliveries[d] > cap:
                deliveries[d] = deliveries[d] - (cap - deliverSum)
                deliverSum = cap
            else:
                deliverSum += deliveries[d]
                d -=1

        while p >=0 and pickupSum < cap:
            if pickupSum + pickups[p] > cap:
                pickups[p] = pickups[p] - (cap - pickupSum)
                pickupSum = cap
            else:
                pickupSum += pickups[p]
                p -=1
    
        answer += 2 * maxDistance
    
    return answer