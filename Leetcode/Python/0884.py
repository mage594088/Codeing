A = "apple apple"
B = "banana"

a = A.split() + B.split()
c = []

dict = {}

for i in range(len(a)):
    if a[i] not in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]] = 2
        
print(dict)

for i in range(len(a)):
    if dict[a[i]] == 1:
        c.append(a[i])

print(c)