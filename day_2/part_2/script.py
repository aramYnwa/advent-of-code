import re

def foo(data):
    sum = 0
    c = {"red" : 0, "green" : 1, "blue" : 2}
    for i in data:
        l = i.replace(",", "").replace(";", "").replace(":", "").replace("\n", "").split(" ")
        t = l[2:]
        l = [1, 1, 1]
        temp = 0
        for i in t:
            if i.isdigit():
                temp = int(i)
            elif i in c:
                a = c.get(i)
                if temp > l[a]:
                    l[a] = temp
            else:
                raise RuntimeError(i)
        sum += l[0] * l[1] * l[2]
            
    return sum


f = open ("example.txt", "r")
data = f.readlines()
assert(foo(data)==2286)


f = open("../input.txt", "r")
data = f.readlines()
print(foo(data))