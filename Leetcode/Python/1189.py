text = "loonbalxballpoon"

dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
for i in range(len(text)):
    if text[i] in dict:
        dict[text[i]] += 1

x = min(dict['b'], dict['a'], int(dict['l']/2), int(dict['o']/2), dict['n'])
print(x)