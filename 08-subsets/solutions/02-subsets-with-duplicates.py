def subsets2_n(nums):
    nums.sort()
    res = [[]]

    prevEnd = 0
    for i in range(len(nums)):
        startIdx = 0
        if i > 0 and nums[i] == nums[i-1]: startIdx = prevEnd 
        
        prevEnd = len(res) 
        for j in range(startIdx, prevEnd):
            cur = res[j].copy()
            cur.append(nums[i])
            res.append(cur)
    
    print(res)

# subsets2_n([1,5,3,3])

def subsets2_b(nums):
    nums.sort()
    res = []
    
    def backtrack(out, i):  
        if i == len(nums):return res.append(out.copy())

        out.append(nums[i])
        backtrack(out, i+1)
        out.pop()

        j = i
        while j < len(nums)-1 and nums[j] == nums[j+1]:
            j += 1

        backtrack(out, j+1)

    backtrack([], 0)
    print(res)

# subsets2_b([1,2,2])