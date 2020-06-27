x = 1534236469

output = ''
dig = len(str(x))

if str(x)[0] != '-':
    for i in range(dig):
        output = output + str(x)[dig-1-i]
else:
    output = output + '-'
    for i in range(1, dig):
        output = output + str(x)[dig-i]

ret = int(output)

if ret > pow(2, 31)-1:
    print(0)
elif ret < -pow(2, 31):
    print(0)
else:    
    print(ret)