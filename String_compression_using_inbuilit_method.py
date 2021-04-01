s='AAABBCCCC'
char_set = sorted(set(s))
mem = []
for char in char_set:
    mem.append(char)
    mem.append(str(s.count(char)))
print("".join(mem))