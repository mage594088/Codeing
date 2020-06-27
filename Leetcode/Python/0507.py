import math
num = 99999992

if num < -2:
    print(False)

a = int(math.sqrt(num))
output = 0
for i in range(1, a+1):
    if num%i == 0:
        output += i
        output += int(num/i)
        

if output == 2*num:
    print(True)
else:
    print(False)
