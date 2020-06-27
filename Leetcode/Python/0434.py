s = "Hello, my name is John"

if s == "":
    print(0)
    
output = 0
for i in range(len(s)-1):
    if s[i] == " " and s[i+1] != " ":
        output += 1
if s[0] != " ":     
    print(output+1)
else:
    print(output)