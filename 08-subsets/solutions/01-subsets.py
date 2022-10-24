# Normal appraoch
def subsets_n(nums):
    res = [[]]

    for n in nums:
        for i in range(len(res)):
            cur = res[i].copy()
            cur.append(n)
            res.append(cur)

    print(res)

# subsets_n([1,5,3])


# Backtracking appraoch
def subsets_b(nums):
    res = []
    def backtrack(out, i):
        if i == len(nums):return res.append(out.copy())

        # not adding nums[i]
        backtrack(out, i+1)

        # adding nums[i]
        out.append(nums[i])
        backtrack(out, i+1)
        
        out.pop()

    backtrack([], 0)
    print(res)

# subsets_b([1,5,3])