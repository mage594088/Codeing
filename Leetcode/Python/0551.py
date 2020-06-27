s = "PPALLL"

count = 0
for i in range(len(s)-2):
     if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
        print(False)
        
for i in range(len(s)):
    if s[i] == 'A':
        if count == 0:
            count += 1
        else:
            print(False)
            
print(True)
        
        