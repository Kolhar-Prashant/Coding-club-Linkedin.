L=[16,17,4,3,5,2]
indx = 0
lead = []
while indx != len(L):
    temp = L[indx+1:]  # List slicing to get new list from current element + 1
    valid = True
    for no in temp:
        if no > L[indx]:
            valid = False
            break
    if valid:
        lead.append(L[indx])
    indx+=1
print(lead)