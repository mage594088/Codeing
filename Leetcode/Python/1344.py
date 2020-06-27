hour = 1
minutes = 57

if hour >= 12:
    hour -= 12
m = minutes*6
h = hour*30 + minutes*6/12

output = max(h, m) - min(h, m)
if output > 180:
    output = 360 - output

print(output)