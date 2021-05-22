def check(k):
    indx = 0
    Flag = False
    while indx != len(L):
        if L[indx] == 1:
            if Flag == True:
                if indx - last_indx < k+1:
                    return False
            last_indx = indx
            Flag = True
        indx+=1
    return True            

L = [1,0,0,0,1,0,0,1]
k = 2 
print(check(k))