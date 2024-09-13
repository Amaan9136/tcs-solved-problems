def is_valid_input(s):
    return all(c == 'M' or c == 'L' for c in s)

def count_valid_combinations(s):
    n = len(s)
    count = 0
    for i in range(n - 2):
        if (s[i] != s[i+1]) and (s[i+1] != s[i+2]) and (s[i] != s[i+2]):
            count += 1
    return count

def determine_winner(ashok_row, anand_row):
    if not (is_valid_input(ashok_row) and is_valid_input(anand_row)):
        return "Invalid input"

    ashok_count = count_valid_combinations(ashok_row)
    anand_count = count_valid_combinations(anand_row)

    if ashok_count > anand_count:
        return "Ashok"
    elif anand_count > ashok_count:
        return "Anand"
    else:
        return "Draw"

#Input
ashok_row = input().strip()
anand_row = input().strip()

#Output 
print(determine_winner(ashok_row, anand_row))
