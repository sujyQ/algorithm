def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    seconds = 0
    going = []
    
    while True :
        if going and going[0] == bridge_length :
            going.pop(0)
            on_bridge.pop(0)
        
        if truck_weights and len(on_bridge) < weight :
            if  sum(on_bridge) + truck_weights[0] <= weight :
                on_bridge.append(truck_weights.pop(0))
                going.append(0)
        
        seconds += 1
        going = [g + 1 for g in going]
        
        if not truck_weights and not on_bridge :
            break
                
    return seconds