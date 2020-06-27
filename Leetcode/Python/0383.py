ransomNote = "aa"
magazine = "aab"

dict = {}
for i in range(len(magazine)):
    if magazine[i] not in dict:
        dict[magazine[i]] = 1
    else:
        dict[magazine[i]] += 1
        
for i in range(len(ransomNote)):
    if ransomNote[i] not in dict:
        print(False)
        break
    else:
        dict[ransomNote[i]] -= 1        
    if dict[ransomNote[i]] == 0:
        del dict[ransomNote[i]]

print(dict)
print(True)