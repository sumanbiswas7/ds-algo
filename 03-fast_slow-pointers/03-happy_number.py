# HAPPY NUMBER :)
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

def isHappy(self, n: int) -> bool:
    slow , fast = n , n
    
    while True:
        slow = self.sumOfSquares(slow)
        fast = self.sumOfSquares(self.sumOfSquares(fast))
        
        if fast == slow: break
    return slow == 1 # -> if slow = 1 return True else retrun False 
    

def sumOfSquares(self, n):
    output = 0
    
    while n != 0:
        digit = n % 10 # -> last digit
        digit = digit ** 2
        output += digit 
        n = n // 10 # -> next last digit
        
    return output
        


def isHappyB(self, n: int) -> bool:
    visit = set()
    
    while n not in visit:
        visit.add(n)
        n = self.sumOfSquares(n)
        
        if n == 1: return True
    
    return False

def sumOfSquares(self, n):
    output = 0
    
    while n != 0:
        digit = n % 10 # -> last digit
        digit = digit ** 2
        output += digit 
        n = n // 10 # -> next last digit
        
    return output
