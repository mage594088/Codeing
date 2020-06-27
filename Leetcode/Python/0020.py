s = '[])'

d = ""
if s=='':
    print(True)
elif len(s)%2 ==1:
    print(False)
elif s[0] == '(' or s[0] == '[' or s[0] == '{':
    d = d + s[0]
    for i in range(1, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            d = d + s[i]
        elif s[i] == ')' and d[-1] =='(':
            d = d[:-1]
        elif s[i] == ']' and d[-1] =='[':
            d = d[:-1]
        elif s[i] == '}' and d[-1] =='{':
            d = d[:-1]
        else:
            print(False)
else:
    print(False)
   
if d == "":
    print(True)
