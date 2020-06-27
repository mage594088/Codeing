n = 10

output = []
output.append('')
output.append('1')
output.append('11')
output.append('21')
output.append('1211')
output.append('111221')

if n <= 5:
    n = n
else:
    for i in range(6, n+1):
        tmp = []
        for j in range(len(output[i-1])):
            tmp.append(output[i-1][j])
        dict = {}
        dict[tmp[0]] = 1
        ans = ''
        
        for j in range(1, len(tmp)):
            if tmp[j] not in dict:
                ans += str(dict[tmp[j-1]])
                ans += tmp[j-1]
                del dict[tmp[j-1]]
                dict[tmp[j]] = 1
            else:
                dict[tmp[j]] += 1
        
        if len(dict) != 0:
            ans += str(dict[tmp[-1]])
            ans += tmp[-1]
        output.append(ans)
        
print(output)
