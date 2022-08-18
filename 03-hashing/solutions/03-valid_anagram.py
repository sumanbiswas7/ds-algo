def isAnagram(s, t):
    char_set = {}
    if len(s) != len(t): return False
    for e in s:
        char_set[e] = 1 + char_set.get(e,0)
    for e in t:
        if e in char_set:
            char_set[e] -= 1
            if char_set[e] == 0: del char_set[e]
    if len(char_set) > 0: return False
    else: return True