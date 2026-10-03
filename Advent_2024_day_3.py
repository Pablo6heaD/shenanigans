#advent of code 2024 day 3
#corrrupted data: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
import re

def mul(a, b):
    return a * b

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

matches = re.findall(r"mul\(\d+,\d+\)", data)

total = 0
for match in matches:
    numbers = re.findall(r"\d+", match)
    a, b = map(int, numbers)
    result = mul(a, b)
    total += result
    print(total)