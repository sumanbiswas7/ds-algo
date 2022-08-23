# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

def stringAnagrams(str , pattern):
    freqMap = {}
    start , match = 0 , 0
    resArr = []

    for c in pattern:
        freqMap[c] = 1 + freqMap.get(c , 0)

    for end in range(len(str)):

        endChar = str[end]
        if endChar in freqMap:
            freqMap[endChar] -= 1
            if freqMap[endChar] == 0: match += 1
        
        if match == len(pattern): resArr.append(start)

        if end >= len(pattern) - 1:
            startChar = str[start]
            start += 1
            if startChar in freqMap:
                if freqMap[startChar] == 0: match -= 1
                freqMap[startChar] += 1

    return resArr




print(stringAnagrams("eidbmaoabmo", "amb"))    

