def checkInclusion(s1,s2):
    start , matched = 0 , 0        
    charFreq = {}

    # P1
    for c in s1:
        charFreq[c] = 1 + charFreq.get(c,0)

    for end in range(len(s2)):
        endChar = s2[end]
        # P2
        if endChar in charFreq:
            charFreq[endChar] -= 1
            if charFreq[endChar] == 0: matched += 1

        if matched == len(charFreq): return True        

        # P3
        if end >= len(s1)-1:
            startChar = s2[start]
            start += 1
            if startChar in charFreq:
                if charFreq[startChar] == 0: matched -= 1
                charFreq[startChar] += 1

    return False


print(checkInclusion("ab", "eidboaoo"))        


# P1 -> adding all the characters with count from s1 in the charFreq map eg:{'char1': num1, 'char2': num2}
# P2 -> decrementing the frequency and incrementing the matched var if needed (when freq == 0) 
# P3 -> starting to shift the window by 1 when the end is exceeded. if previous window had char present in charFreq then
# updating the freqency and updating the match if the match was affected (freq == 0)   
