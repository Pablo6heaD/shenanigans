#advent of code 2024 day 2

levels =[[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1]]
# def check_safety(reports):
#     differences = []
#     chceck_sign = 0
#     for report in reports:
#         for i in range(1, len(report)):
#             differences.append(report[i] - report[i-1])
#         chceck_sign = all(d >= 0 for d in differences) and all(d < 3 for d in differences)
#     return chceck_sign


def check_safety(report):
    differences = []
    chceck_sign = 0
    for entry in range(1, len(report)):
        differences.append(report[entry-1] - report[entry])
    print(differences)
    chceck_sign = all(d >= 0 for d in differences) and all(d < 3 for d in differences)
    return chceck_sign

print(check_safety(levels[0]))