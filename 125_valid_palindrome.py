import re

class Solution(object):

  def _clean_string(self, s):
    s = re.sub(r'\W+', '', s).lower()
    return s

  def isPalindrome(self, s):
      """
      :type s: str
      :rtype: bool
      """
      s = self._clean_string(s)
      return s == s[::-1]

soln = Solution()
s = 'A man, a plan, a canal: Panama'
print(soln.isPalindrome(s))