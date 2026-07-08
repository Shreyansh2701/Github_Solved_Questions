class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            totalsum = 0
            while n>0:
                d = n % 10
                n = int(n / 10)
                totalsum = totalsum + (d*d)
            return totalsum
        
        slow = fast = n
        while fast != 1:
            slow = square(slow)
            fast = square(fast)
            fast = square(fast)
            if slow == fast and slow != 1:
                return False
        return True
    
    