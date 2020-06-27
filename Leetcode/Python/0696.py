s = "00110"

n = len(s)
count = 0
for i in range(n-1):
    if s[i:i+2] == '01':
        for j in range(min(i+1, n-i-1)):
            if s[i-j] == '0' and s[i+1+j] == '1':
                print(s[i-j:i+j+2])
                count += 1
            else:
                break
            
    elif s[i:i+2] == '10':
        for j in range(min(i+1, n-i-1)):
            if s[i-j] == '1' and s[i+1+j] == '0':
                print(s[i-j:i+j+2])
                count += 1
            else:
                break

print(count)