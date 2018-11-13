import math

class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
      return 1
    
    delta = 0.1

    lower = 1
    upper = int(math.ceil(x / 2))

    while lower < upper:
      middle = (upper + lower) // 2
      
      if math.abs(middle**2 - x) <= delta:
        return middle
      elif middle**2 > x:
        upper = middle
      elif middle**2 < x:
        upper = lower

soln = Solution()
print(soln.mySqrt(2))