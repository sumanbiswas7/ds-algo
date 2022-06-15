def lenDistinct(nums):
    l , r = 0 , 1
    res = []
    while r < len(nums):
        if nums[l] != nums[r]:
            if len(res) > 0 and res[-1] == nums[r]:
                res.append(nums[r])
            else:
                res.append(nums[l])
                res.append(nums[r])

        # elif r == len(nums) - 1 and nums[l] != nums[r]: res.append(nums[r])


        l += 1
        r += 1

    print(res)



nums = [2, 3, 3, 3, 6, 9, 9]
lenDistinct(nums)

a = [2]
if a:
    print("hi")

