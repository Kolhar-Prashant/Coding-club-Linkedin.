
L = [5,11,10, 20, 9, 16, 23]
mem = []
Dict = {}
for num in L:
    cnt = 0
    for divisor in range(2,num-1):
        if num % divisor == 0:
            cnt += 1
    mem.append(cnt)
    Dict[num]=cnt
    mem = sorted(mem,reverse=True)
Facts = []
for cnt in mem:
    for num,count in Dict.items():
        if cnt == count:
            Facts.append(num)
            Dict[num]='NA'
            break
print(Facts)

