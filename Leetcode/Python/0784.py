S = "3z4"

dict = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
num = len(S)
count = 0
for i in range(num):
    if S[i] not in dict:
        count += 1

case = []
k = len(str(bin(pow(2, count))[2:]))

for i in range(pow(2, count)):
    tmp = str(bin(i)[2:])
    word = ""
    if  len(tmp) < k:
        for i in range(k-len(tmp)-1):
            word += '0'
        word += tmp
    else:
        word += tmp
    case.append(word)

output = []
for j in range(pow(2, count)):
    almo = ""
    l = 0
    for i in range(num): 
        
        if S[i] in dict:
            almo += S[i]
        else:
            while l <= k:
                if case[j][l] == '1':
                    almo += S[i].upper()
                    l += 1
                    break
                else:
                    almo += S[i].lower()
                    l += 1
                    break
    output.append(almo)

print(output)
        
    