def remove_doublespace(s):    
    L=[]
    space_cnt=0
    for char in s:
        if char == " ":
            space_cnt+=1
        else:
            space_cnt=0
        if space_cnt  < 2:
            L.append(char)
    return "".join(L)

s = "  le   good     a a  a "
s=s.strip()
print(remove_doublespace(s))
