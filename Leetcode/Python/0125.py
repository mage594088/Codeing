s = "Marge, let's \"went.\" I await news telegram."

t = ""
dict = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z'}
for i in range(len(s)):
    if s[i].lower() in dict:
        t += s[i].lower()

print(t)

count = 0
for i in range(len(t)//2):
    if t[i] != t[len(t)-1-i]:
        count += 1
        
if count != 0:
    print(False)
else:
    print(True)
    