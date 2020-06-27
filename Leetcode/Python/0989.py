A = [2,1,5]
K = 806

output = []
k = str(K)
klen = len(k)
alen = len(A)
kstr = []

if alen - klen > 0:
    output.append(0)
    for i in range(alen - klen + 1):
        kstr.append(0)
elif alen == klen:
    output.append(0)
    kstr.append(0)
elif alen - klen < 0:
    kstr.append(0)
    for i in range(klen - alen + 1):
        output.append(0)

for i in range(alen):
    output.append(A[i])

for i in range(klen):
    kstr.append(K//pow(10, klen-i-1)%10)


tlen = len(kstr)

for i in range(tlen):
    t = kstr[tlen -1 - i] + output[tlen -1 - i]
    if t < 10:
        output[tlen -1 - i] = t
    else:
        output[tlen -1 - i] = t-10
        output[tlen -2 - i] += 1 

print(output)

if output[0] == 0:
    output = output[1:]

print (output)

