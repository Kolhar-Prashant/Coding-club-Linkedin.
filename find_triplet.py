nums=[9,2,1,7,4,-8,14]
nums = sorted(nums)
a=0
b=1
c=len(nums)-1
mem = []
tar = 12
while a != len(nums)-2:
    while c > b:
        sum = nums[a] + nums[b] + nums[c]
        if sum == tar:
            temp=[]
            temp.append(nums[a])
            temp.append(nums[b])
            temp.append(nums[c])
            mem.append(temp)
            b+=1
            c-=1
            continue
        if sum > tar:
            c -= 1
        if sum < tar:
            b += 1
    a += 1
    b=a+1
    c=len(nums)-1
print(mem)