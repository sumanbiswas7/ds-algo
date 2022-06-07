# 424. Longest Repeating Character Replacement


def characterReplacement(self, s, k):
    charCount = {}
    win_start = 0
    max_len = 0
    
    for win_end in range(len(s)):
        charCount[s[win_end]] = 1 + charCount.get(s[win_end],0)
        
        while ((win_end-win_start + 1) - max(charCount.values())) > k:
            charCount[s[win_start]] -= 1
            if charCount[s[win_start]] == 0:
                      del charCount[s[win_start]]
                      
            win_start += 1
        
        max_len = max(max_len , win_end-win_start+1)
    
    
    return max_len
                      
# characterReplacement("AABABBA",1)
# characterReplacement("AABA",0)
characterReplacement("AABABBA",3)
