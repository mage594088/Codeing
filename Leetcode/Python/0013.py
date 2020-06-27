s = "IV"

output = 0
dict = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for i in range(len(s)):
    if i > 0 and dict[s[i]] > dict[s[i-1]]:
        output += dict[s[i]] - 2 * dict[s[i-1]]
    else:
        output += dict[s[i]]    

print(output)


