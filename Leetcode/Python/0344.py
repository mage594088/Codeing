s = ["h","e","l","l","o"]

for i in range(len(s)//2):
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    
print(s)