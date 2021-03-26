def check(l):
    a=0
    b=1
    start_indx=0
    stop_indx=0
    while b!=len(l):
        if l[b] < l[a]:
            if start_indx == 0:
                start_indx=a
        if start_indx != 0 and l[b] > l[a]:
            stop_indx=a
            return start_indx,stop_indx     # returning when a subarray is found
        a+=1
        b+=1
    if start_indx != 0:  # performing check if subarry is found unsorted, but array is completed.
        return start_indx, len(l)-1
    else:
        return -1,-1  # returning when array is already sorted

l=[1,2,5,4,3,9]
a,b = check(l)
if a == -1 and b == -1:
    print(False)
else:
    print("Yes")
    print(l[a:b+1])
