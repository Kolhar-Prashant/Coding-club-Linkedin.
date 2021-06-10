
def compute(L):
    Dict = {}
    for word in L:
        for char in word:
            if char not in Dict:
                Dict[char]=1
            else:
                Dict[char]+=1
    mem = []
    for char, count in Dict.items():
        freq = count//len(L)
        for _ in range(freq):
            mem.append(char)
    return mem

L = ["hello","lool","roll"]
print(compute(L))