def alphabet(s):
    l = [] 
    for i in range(len(s)):
        if s[i] == ' ': continue
        else:
            if s[i] not in l: l.append(s[i].lower())
    if len(l) == 26: return True
    else: return False
print(alphabet("The quick brown fox jumps over the lazy dog"))