import operator
paragraph = "a, a, a, a, b,b,b,c, c"
banned= ["a"]

p = {',', '.', '/', '?', ';', '!', '"', '\''}
paragraph2 = ""
for i in range(len(paragraph)):
    if  paragraph[i] in p:
        paragraph2 += " "
    else:
        paragraph2 += paragraph[i]

p = len(paragraph2)
word = []
tmp = ""

for i in range(p):
    if paragraph2[i] != " ":
        tmp+=paragraph2[i].lower()
    else:
        if len(tmp) != 0:
            word.append(tmp)
            tmp = ""

word.append(tmp)

dict = {}
print(word)       

if banned == []:
    for i in range(len(word)):
        if word[i] not in dict:
            dict[word[i]] = 1
        else:
            dict[word[i]] += 1
else:
    for i in range(len(word)):
        ban = 0
        for j in range(len(banned)):
            if word[i] == banned[j]:
                ban = 1
                
        if ban == 0:
            if word[i] not in dict:
                dict[word[i]] = 1
            else:
                dict[word[i]] += 1
print(dict)
k = max(dict.items(), key=operator.itemgetter(1))[0]
print(k)

