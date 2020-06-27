import math
c = 25

a = int(math.sqrt(c))
print(a)

for i in range(a+1):
    j = int(math.sqrt(c - i*i)) 
    if c - i*i == j*j:
        print(i, j, True)
        break
    elif c - i*i == (j+1)*(j+1):
        print(i, j, True)
        break
        
print(False)

