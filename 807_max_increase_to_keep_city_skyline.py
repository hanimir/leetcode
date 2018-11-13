class Solution(object):
  def test_from_leetcode(self):
    print('Running test_from_leetcode...')
    grid = [
      [3,0,8,4],
      [2,4,5,7],
      [9,2,6,3],
      [0,3,1,0]]
    
    expected = 35
    actual = self.maxIncreaseKeepingSkyline(grid)
    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_from_leetcode')
      raise e
    else:
      print('Passed test_from_leetcode!')

  def runTests(self):
    self.test_from_leetcode()

  def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    transposed = list(zip(*grid))
    difference = 0
    for i in range(len(grid)):
      for j in range(len(grid)):
        difference += min(max(grid[i]), max(transposed[j])) - grid[i][j]
    
    return difference

soln = Solution()
soln.runTests()