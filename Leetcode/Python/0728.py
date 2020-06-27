left = 1
right = 22

output = []

for i in range(left, right+1):
    a = str(i)    
    t = 0   
    for j in range(len(a)):
        if int(a[j]) == 0:
            t = 1
        elif i%int(a[j]) != 0:
            t = 1
    if t == 0:
        output.append(i)
            
print(output)
