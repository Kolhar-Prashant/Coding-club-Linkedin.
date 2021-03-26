#start from a=0,b=1 if b < a mark start indx and keep track of max element
 #if L[b] element is greater than max element then mark stop indx on a

L = [10,12,20,30,25,40,32,31,35,50,60]
a=0
b=1
start_indx =0
stop_indx  =0
maxx = 0
while b != len(L)-1:
    if L[b] < L[a] and start_indx == 0:
        start_indx = a
    if start_indx != 0:
        if L[a] > maxx:
            maxx = L[a]
    if L[b] > L[a] and L[b] > maxx:
        stop_indx = a
    a+=1
    b+=1
print(start_indx,stop_indx)
