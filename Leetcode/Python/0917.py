S = "a-bC-dEf-ghIj"

dict = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v','w','x','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V','W','X','X','Y','Z'}

tmp = []
output = ""

for i in range(len(S)):
    if S[i] in dict:
        tmp.append(S[i])
        
j = 1        
for i in range(len(S)):
    if S[i] in dict:
        output += tmp[len(tmp) - j]
        j+=1
    else:
        output += S[i]
        
print(output)