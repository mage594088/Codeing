s =  "  "

if len(s) == 0:
    print(0)
    
t = ""
for i in range(len(s)):
    t += s[len(s)-i-1]

output = []
tmp = ""

space = 0
k = 0
for i in range(len(t)):
    if t[i] != ' ':
        tmp += t[i]
        space += 1
        k += 1
    else:
        if space != 0:
            output.append(tmp)
            break
    
if space != 0:
    output.append(tmp)
elif k == 0:
    print(0)

print (len(output[0]))

    
    
