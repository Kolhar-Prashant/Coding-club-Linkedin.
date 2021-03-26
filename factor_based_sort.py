def calc_no_facts(n):
    cnt = 0
    for divisor in range(2,n-1):
        if n % divisor == 0:
            cnt += 1
    return cnt

L = [5,11,10, 20, 9, 16, 23]
Dict = {}
mem = []
for num in L:
    cnt = calc_no_facts(num)
    mem.append(cnt)
    Dict[num]=cnt
mem = sorted(mem,reverse=True)

Facts = []
for cnt in mem:
    for num,count in Dict.items():
        if cnt == count:
            Facts.append(num)
            Dict[num]="NA"
            break
print(Facts)