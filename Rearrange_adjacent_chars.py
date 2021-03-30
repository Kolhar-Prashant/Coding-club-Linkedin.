s='AAABC'
t=[]
last_char = '-'
valid = False
temp = []
for char in s: 
    if last_char != char:
        t.append(char)
        if valid == True:
            if len(temp) > 0:
                t.append(temp[0])
                temp.pop(0)            
    else:
        temp.append(char)    
        valid = True
    if len(t) < 1:
        last_char = char
    else:
        last_char = t[-1]
s="".join(t)
print(s)