class Solution(object):
  def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    jewels = set(J)
    num_jewels = 0
    for stone in S:
      if stone in jewels:
        num_jewels += 1
    
    return num_jewels

soln = Solution()
J = 'z'
S = 'Z'
print(soln.numJewelsInStones(J, S))