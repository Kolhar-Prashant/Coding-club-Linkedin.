nums = [3,4,5,2]
a,b = 0,1
max_sum = 0
while a != len(nums)-1:
    while b != len(nums):
        t = ((nums[a]-1) * (nums[b]-1))
        if t > max_sum:
            max_sum = t
        b+=1
    a+=1
    b=a+1
print(max_sum)
