import math

def is_triangular(num):
    n = (-1 + math.sqrt(1 + 8 * num)) / 2
    return n.is_integer()

def weapon_boxes(boxes, N, K):
    n = len(boxes)
    shifted_boxes = []
    unshifted_counter = 0  
    cycle_box = boxes[0]   
    while unshifted_counter < K:
        selected_boxes = boxes[:N]
        for i in range(N-1):
            if selected_boxes[i] < selected_boxes[i+1]:
                shifted_boxes.append(selected_boxes[i])
                boxes.append(boxes.pop(0))  
            else:
                shifted_boxes.append(selected_boxes[i+1])
                boxes.append(boxes.pop(1))
        
        if boxes[0] == cycle_box:
            unshifted_counter += 1
        else:
            cycle_box = boxes[0]
            unshifted_counter = 0
    total_cost = sum(weight for weight in shifted_boxes if not is_triangular(weight))
    return total_cost

boxes = list(map(int, input().split()))
N, K = map(int, input().split())

# output
print(weapon_boxes(boxes, N, K))
