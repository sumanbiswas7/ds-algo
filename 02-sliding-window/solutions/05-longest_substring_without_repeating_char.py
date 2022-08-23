def lengthOfLongestSubstring(s):
    charSet = set()
    win_start = 0
    res = 0
    for win_end in range(len(s)):
        while s[win_end] in charSet:
            charSet.remove(s[win_start])
            win_start += 1

        charSet.add(s[win_end])

        res = max(win_end-win_start+1, res)

    print(res)


lengthOfLongestSubstring("abccde")

        

