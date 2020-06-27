candies = [1,1,1,1,2,2,2,3,3,3]

num = len(candies)
dict = {}
output1 = []
output2 = []
for i in range(num):
    if candies[i] not in dict:
        dict[candies[i]] = 1
        if len(output1) < num/2:
            output1.append(candies[i])
        else:
            c = num/2
            output2.append(candies[i])
    else:
        if len(output2) < num/2:
            dict[candies[i]] += 1
            output2.append(candies[i])
        else:
            output1.append(candies[i])

dict = {}
for i in range(len(output1)):
    if output1[i] not in dict:
        dict[output1[i]] = 1

print(len(dict))