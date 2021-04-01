s='AAABBCCCC'
mem=[]
last_char=s[0]
cnt=1
for char in s[1:]:
    if char != last_char:
        mem.append(last_char)
        mem.append(str(cnt))
        cnt=1
    else:
        cnt+=1
    last_char=char
mem.append(last_char)
mem.append(str(cnt))
print("".join(mem))           