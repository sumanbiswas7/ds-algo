def productExceptSelf(nums):
    output = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
            
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        output[i] *= postfix
        postfix *= nums[i]
        
    return output