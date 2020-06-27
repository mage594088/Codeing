x = 0

dig = len(str(x))
count = 0
if x < 0:
    print(False)
elif x==0:
    print(True)
else:
    if(dig%2 == 0):
        print(dig%2)
        for i in range(dig/2):
            if(str(x)[i] == str(x)[dig-1-i]):
                count+=1
        if(count == dig/2):
            print(True)
        else:
            print(False)
    else:
        for i in range(int((dig-1)/2)):
            if(str(x)[i] == str(x)[dig-1-i]):
                count+=1
        if(count == (dig-1)/2):
            print(True)
        else:
            print(False)
