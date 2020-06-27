rowIndex = 3

output = []
s = []
s.append(1)
i = 1
n = rowIndex+2
for k in range(1, n):
	t = []
	s.append(s[i-1]*i)
	i+=1    

	for j in range(k):    
		t.append(int(s[k-1]/(s[k-1-j]*s[j])))

	output.append(t)
print(output[rowIndex])