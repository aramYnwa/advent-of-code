import re

c = {"red" : 12, "green" : 13, "blue" : 14}

def foo(data):
    sum = 0
    for i in data:
        l = i.replace(",", "").replace(";", "").replace(":", "").replace("\n", "").split(" ")
        _, id = l[:2]
        t = l[2:]
        impposible = True
        temp = 0
        for i in t:
            if i.isdigit():
                temp = int(i)
            elif i in c:
                if temp > c.get(i):
                    impposible = True
                    break
            else:
                raise RuntimeError(i)
            impposible = False
        if not impposible:
            sum += int(id)
    return sum


f = open ("example.txt", "r")
data = f.readlines()
assert(foo(data)==8)


f = open("../input.txt", "r")
data = f.readlines()
print(foo(data))