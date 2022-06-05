# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".


def longestSubstrWithKChar(s,k):
    charSet = set()
    res = 0
    l = 0
    for r in range(len(s)):
        charSet.add(s[r])

        while len(charSet) > k:
            if s[l] in charSet:
                charSet.remove(s[l])
            l += 1

        res = max(r-l+1, res)
        
    print(res)




inp="araaci"
k=2

longestSubstrWithKChar("cbbebi", 3)

