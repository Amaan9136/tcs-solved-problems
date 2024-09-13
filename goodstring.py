def find_nearest_good_letter(char, good_string, prev_good):
    nearest_good = None
    min_distance = float('inf')

    for good_char in good_string:
        distance = abs(ord(char) - ord(good_char))
        if distance < min_distance:
            min_distance = distance
            nearest_good = good_char
        elif distance == min_distance:
            if abs(ord(prev_good) - ord(good_char)) < abs(ord(prev_good) - ord(nearest_good)):
                nearest_good = good_char

    return nearest_good, min_distance

def calculate_total_distance(good_string, name):
    total_distance = 0
    prev_good = good_string[0]

    for char in name:
        if char in good_string:
            continue  
        nearest_good, distance = find_nearest_good_letter(char, good_string, prev_good)
        total_distance += distance
        prev_good = nearest_good

    return total_distance

#input
good_string = input().strip()
name = input().strip()

#output
print(calculate_total_distance(good_string, name))
