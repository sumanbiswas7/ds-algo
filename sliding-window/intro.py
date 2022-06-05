# Sliding Window

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Averages of subarrays of size K: [2.2, 2.8, 2.4, 3.6, 2.8]

input = [1, 3, 2, 6, -1, 4, 1, 8, 2]

def avgSubArrB(nums,k):
    res = []
    for i in range(len(nums)-k+1):
        j = i
        temp = 0
        while j < i + k:
            temp += nums[j]
            j += 1
        res.append(temp/k)
    print(res)



def avgSubArr(nums,k):
    res = []
    i = 0
    tempAvg = 0
    while i < k:
        tempAvg += nums[i]
        i += 1
    res.append(tempAvg/k)

    while i < len(nums):
        tempAvg += nums[i]
        tempAvg -= nums[i-k]
        res.append(tempAvg/k)
        i += 1

    print(res)




input = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avgSubArr(input, 5)
