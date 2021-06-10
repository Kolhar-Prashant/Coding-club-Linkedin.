def find(s,k):
    a=0
    b=k
    vowel_list = ['a','e','i','o','u']
    max_len=0
    while b != len(s)+1:
        temp = s[a:b]
        cnt=0
        for char in temp:
            if char in vowel_list:
                cnt+=1
        if cnt > max_len:
            max_len = cnt
        a+=1
        b+=1
    return max_len

s = "abciiidef"
k = 3
print(find(s,k))
