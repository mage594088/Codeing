words = ["gin", "zen", "gig", "msg"]

dict = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
output = 0
dict2 = {}

for i in range(len(words)):
    tmp = ""
    for j in range(len(words[i])):      
        if words[i][j] in dict:
            tmp += dict[words[i][j]]

    if tmp not in dict2:
        dict2[tmp] = 1
    
            
print(len(dict2))