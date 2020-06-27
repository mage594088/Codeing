name = "vtkgn"
typed = "vttkgnn"

num = 0
count = 0
for i in range(len(typed)):
    if typed[i] == name[num]:
        count += 1
        num += 1
    if num == len(name):
        break
    
if count == len(name):
    print(True)
else:
    print(False)