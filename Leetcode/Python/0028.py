haystack = "a"
needle = "a"

if needle == "":
    print(0)
else:
    output = 0
    h = len(haystack)
    n = len(needle)
    for i in range(h-n+1):
        tmp = 0
        for j in range(n):
            if haystack[i+j] == needle[j]:
                tmp += 1
        if tmp == n:
            print(i)
            break
            
    print(-1)