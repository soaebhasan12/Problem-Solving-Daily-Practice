# Strivers Solution
class Solution:
    def GCD(self, n1, n2):
        n1 = abs(n1)
        n2 = abs(n2)

        while n2 != 0:
            temp = n2
            n2 = n1 % n2
            n1 = temp
        
        return n1
      
      
      
      
      
      
      
      
      
# Leet Code Problem Solution (https://leetcode.com/problems/gcd-of-odd-and-even-sums/)
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # if n % 2 == 0:
        #     sumEven = 0
        #     sumEven_list = []
        #     for i in range(n, 2):
        #         sumEven_list = sumEven_list.append(i)
        #     for value in sumEven_list:
        #         sumEven = sumEven + value

        # if n % 2 != 0:
        #     sumOdd = 0
        #     sumOdd_list = []
        #     for i in range(n, 2):
        #         sumOdd_list = sumOdd_list.append(i)
        #     for value in sumOdd_list:
        #         sumOdd = sumOdd + value

        # while sumOdd or sumEven != 0:
        #     temp = sumOdd
        #     sumOdd = sumEven % sumOdd
        #     sumEven = temp

        
        sumOdd = n*n
        sumEven = n * (n+1)
        
        return n
