# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".


def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
    char_set = {}
    win_start = 0
    max_len = 0
    for win_end in range(len(s)):
        end_char = s[win_end]
        char_set[end_char] = 1 + char_set.get(end_char,0)
        while len(char_set) > k:
            start_char = s[win_start]
            char_set[start_char] -= 1
            if char_set[start_char] == 0:
                del char_set[start_char]
            win_start += 1
        max_len = max(max_len , win_end-win_start+1)
        
    return max_len

def attempt2(s,k):
    #! NOT WORKING 
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



