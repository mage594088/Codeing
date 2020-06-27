word = "Google"

dict = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
output = 0
if len(word) <= 1:
    output = 0

if word[0] not in dict:
    for i in range(1, len(word)):
        if word[i] in dict:
            output = 1

else:  
    if word[1] not in dict:
        for i in range(2, len(word)):
            if word[i] in dict:
                output = 1
    else:
        for i in range(2, len(word)):
            if word[i] not in dict:
                output = 1
    

if output == 0:
    print(True)
else:
    print(False)