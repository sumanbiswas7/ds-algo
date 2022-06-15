def lenDistinct(nums):
    l , r = 0 , 1
    res = []
    while r < len(nums):
        print("---------------------")
        print("l - ",l, " r - ",r,res)

        if nums[l] != nums[r]:
            if res:
                if res[-1] == nums[r] or res[-1] == nums[l]:
                    res.append(nums[r])
            else:
                res.append(nums[l])
                res.append(nums[r])

        if r == len(nums) - 1 and nums[l] == nums[r]: res.append(nums[r])


        l += 1
        r += 1

    print(res)



nums = [2, 3, 3, 3, 6, 9, 9]
nums = [2, 2, 2, 2, 4, 2]
lenDistinct(nums)

