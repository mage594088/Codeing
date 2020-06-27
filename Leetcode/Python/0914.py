deck = [1,2,3,4,4,3,2,1]

dict = {}
for i in range(len(deck)):
    if deck[i] not in dict:
        dict[deck[i]] = 1
    else:
        dict[deck[i]] += 1
        
k = min(dict.items(), key=lambda x: x[1]) 

gcd = dict[k[0]]
if gcd == 1:
    print(False)

l = []
for i in range(2, gcd+1):
    if gcd%i == 0:
        l.append(i)
print(l)


for i in range(len(l)):
    output = 0
    for j in range(len(deck)):
        if dict[deck[j]]%l[i] != 0:
            output = 1
    if output == 0:
        print(True)  

print(False)