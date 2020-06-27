s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"

t = ""
for i in range(len(s)):
    t += s[len(s)-i-1]

dict = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '#01':'j' ,'#11':'k', '#21':'l', '#31':'m', '#41':'n', '#51':'o', '#61':'p', '#71':'q', '#81':'r', '#91':'s', '#02':'t', '#12':'u', '#22':'v', '#32':'w', '#42':'x', '#52':'y', '#62':'z'}
output = ""
i = 0
while i < len(t):  
    if t[i] == '#':
        if t[i:i+3] in dict:
            
            output = output + dict[t[i:i+3]]
            i = i+3
    else:
        output = output + dict[t[i]]
        i+=1
ans = ""        
for i in range(len(output)):
    ans += output[len(output)-i-1]
    
print(ans)