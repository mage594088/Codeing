s = "rat"
t = "car"

if len(s) != len(t):
    print(False)
dig = len(s)

dict1 = {}
dict2 = {}

for i in range(dig):
    if s[i] not in dict1:
        dict1[s[i]] = 1
    elif s[i] in dict1:
        dict1[s[i]] += 1
    if t[i] not in dict2:
        dict2[t[i]] = 1
    elif t[i] in dict2:
        dict2[t[i]] += 1

print(dict1, dict2)
 
for i in range(dig):
    if str(s[i]) in dict2:
        if dict1[str(s[i])] != dict2[str(s[i])]:
            print(False)
    else:
        print(False)

print(True)