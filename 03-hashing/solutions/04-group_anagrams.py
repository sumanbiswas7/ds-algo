def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    char_set = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            if tuple(count) not in char_set: char_set[tuple(count)] = []
            char_set[tuple(count)].append(s)
            
    return char_set.values()