L=[12,10,102,31,15]
mem = []
Dict = {}
for nums in L:
    s = str(nums)  # for looping
    sum = 0
    for digit in s:
        sum+= int(digit)   # looping and summation
    mem.append(sum)
    Dict[nums]=sum
L=[]
mem = sorted(mem)
for sum_no in mem:
    for no, sum in Dict.items():
        if sum_no == sum:
            L.append(no)
            Dict[no]='NA'   # if same count is found, masking it with 'NA' to avoid reprinting.
            break       # breaking the loop once match is found to avoid reprinting.
print(L)

