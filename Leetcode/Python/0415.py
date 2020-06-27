num1 = "40"
num2 = "50"

output = ""
n1 = 0
n2 = 0

dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
for i in range(len(num1)):
    n1 += dict[num1[i]] * pow(10, len(num1)-i-1)
for i in range(len(num2)):
    n2 += dict[num2[i]] * pow(10, len(num2)-i-1)
    
n3 = n1+n2


for i in range(len(str(n3))):
    output += str(n3)[i]

print(output)