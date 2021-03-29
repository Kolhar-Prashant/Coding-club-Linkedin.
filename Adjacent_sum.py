L = [6, 8, 7, 6]
a=0
b=2
max=0
d={}
while a != len(L)-2:
    while b != len(L):
        sum = L[a]+L[b]
        if sum > max:
            dict={}
            max = sum
            temp = []
            temp.append(a)
            temp.append(b)
            dict[max]=temp
            d=dict
        b+=1
    a+=1
    b=a+2
print(d[max])