list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

if len(list1) > len(list2):
    list1, list2 = list2, list1
    
a = len(list1)
b = len(list2)
C = []
dict = {}
c = []


for i in range(a):
    if list1[i] not in dict:
        dict[list1[i]] = 1
        
        
for i in range(b):
    if list2[i] in dict:
        C.append(list2[i])
        c.append(i)

sum = 1000000
output = []
k = 0
for i in range(len(c)):
    for j in range(a):
        if list2[c[i]] == list1[j]:
            if sum > c[i] + j:
                sum = c[i] + j
                k = j
                output.append(list1[k])
            elif sum == c[i] + j:
                k = j
                output.append(list1[k])

print(output) 