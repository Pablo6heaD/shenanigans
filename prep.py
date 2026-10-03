#advent of code 2024 day 1

location_id = [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]
left_side = sorted(location_id[0])
right_side = sorted(location_id[1])

def find_total_distance(left_side, right_side):
    total_distance = 0
    for i in range(len(left_side)):
        total_distance += abs(left_side[i] - right_side[i])
    return total_distance

print(find_total_distance(left_side, right_side))