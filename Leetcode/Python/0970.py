import math
x = 2
y = 1
bound = 10

if x==1:
    a = 1
else:
    a = int(math.log(bound, x))
if y==1:
    b = 1
else:
    b = int(math.log(bound, y))
dict = {}

for i in range(a+1):
    for j in range(b+1):
        if pow(x, i) + pow(y, j) <= bound:
            dict[pow(x, i) + pow(y, j)] = 1

print(sorted(dict.keys()))