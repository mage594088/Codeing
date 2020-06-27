N = 857

output = 0
for i in range(N+1):
    k = str(i)
    t = 0
    count = 0
    for j in range(len(k)):
        if k[j] == '3' or  k[j] == '4' or k[j] == '7':
            t = 1
        elif k[j] == '1' or  k[j] == '0' or k[j] == '8':
            count += 1
    if t == 0 and count!=len(k):
        print(k)
        output+=1

print()
print(output)