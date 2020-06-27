s = "aA"

dict = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
output = []
for i in range(len(s)):
    if s[i] in dict:
        output.append(s[i])

ans = ""
k = 1
for i in range(len(s)):
    if s[i] not in dict:
        ans += (s[i])
    else:
        ans += (output[len(output)-k])
        k += 1
        
print(ans)