moves = "UD"

dict = {'U':0, 'D':0, 'L':0, 'R':0}
for i in range(len(moves)):
    dict[moves[i]] += 1

if dict['U'] == dict['D'] and dict['L'] == dict['R']:
    print(True)
else:
    print(False)
    