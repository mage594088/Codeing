s = "Let's take LeetCode contest"

word = ""
tmp = ""
count = 0
for i in range(len(s)+1):
    if i == len(s):
        for j in range(len(tmp)):
            word += (tmp[len(tmp)-1-j])
    elif s[i] != ' ':
        tmp += s[i]    
    else:
        for j in range(len(tmp)):
            word += (tmp[len(tmp)-1-j])
        word += (" ")
        tmp = ""
        
print(word)