def find_duplicates(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1

    duplicates = []
    for n in range(len(nums)):
        if (nums[n] != n+1): duplicates.append(nums[n])

    return duplicates 