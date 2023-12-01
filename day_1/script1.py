import re

def foo(data):
    sum = 0
    for i in data:
        matches = re.findall(r"([0-9]+)", i)
        n = int(matches[0][0]) * 10 + int(matches[-1][-1])
        print(n)
        sum += n
    return sum

f = open ("example.txt", "r")
data = f.readlines()
assert(foo(data) == 142)


f = open("input.txt", "r")
data = f.readlines()
print(foo(data))