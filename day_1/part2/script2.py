import re

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}


def foo(data):
    sum = 0
    for i in data:
        matches = re.findall(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])", i)[0]
        matches_r = re.findall(r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])", i[::-1])[0]
        n = int(nums.get(matches, matches)) * 10 + int(nums.get(matches_r[::-1], matches_r[::-1]))
        sum += n
    return sum  

f = open("../input.txt", "r")
data = f.readlines()
assert(foo(data) == 53340)
print(foo(data))
