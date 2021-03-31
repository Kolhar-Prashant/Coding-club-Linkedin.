def rev_str(temp):
    mem_s=[]
    t_indx=len(temp)-1
    while t_indx != -1:
        mem_s.append(temp[t_indx])
        t_indx-=1
    temp = "".join(list(mem_s))
    return temp
    
s="This is the best"
mem = []
temp = []
for indx in reversed(range(len(s))):
    if s[indx] != " ":
        temp.append(s[indx])
    else:        
        mem.append(rev_str(temp))
        temp=[]
mem.append(rev_str(temp))
print(mem)    