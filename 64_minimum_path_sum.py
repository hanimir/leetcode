import math


class Solution(object):
  def minPathSum(self, grid):
    if len(grid) == 0 or len(grid[0]) == 0:
      return 0

    min_path_sum_including_element = [[math.inf for i in range(len(grid[0]))] for j in range(len(grid))]
    min_path_sum_including_element[0][0] = grid[0][0]

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if i == j == 0:
          continue

        min_path_sum_up_to_element = math.inf
        if 0 <= j - 1:
          min_path_sum_up_to_element = min(min_path_sum_up_to_element, min_path_sum_including_element[i][j - 1])
        if 0 <= i - 1:
          min_path_sum_up_to_element = min(min_path_sum_up_to_element, min_path_sum_including_element[i - 1][j])

        min_path_sum_including_element[i][j] = min_path_sum_up_to_element + grid[i][j]

    return min_path_sum_including_element[-1][-1]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_leetcode_example(self):
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]]

    expected = 7
    actual = self.solution.minPathSum(grid)

    assert actual == expected

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
