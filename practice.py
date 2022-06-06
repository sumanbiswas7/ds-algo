def longestSubStrWithKdist(str,k):
    window_start = 0
    max_len = 0
    char_set = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        char_set[right_char] = 1 + char_set.get(right_char, 0)

        while len(char_set) > k:
            left_char = str[window_start]
            char_set[left_char] -= 1
            if char_set[left_char] == 0:
                del char_set[left_char]
            window_start += 1

        max_len = max(max_len, window_end-window_start+1)

    print("ans - ",max_len)


longestSubStrWithKdist("araaci", 2)
