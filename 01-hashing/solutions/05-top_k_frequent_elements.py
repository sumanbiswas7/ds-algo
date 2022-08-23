def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    char_set = {}
    freq = [[] for i in range(len(nums))]
        
    for n in nums: char_set[n] = 1 + char_set.get(n,0)
    for n, c in char_set.items(): freq[c].append(n)
            
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k: return res