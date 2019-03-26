class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m == 0 or n == 0:
      return 0

    unique_paths_to_here = [[0] * m for i in range(n)]
    unique_paths_to_here[0][0] = 1

    for i in range(n):
      for j in range(m):
        if i == j == 0:
          continue

        unique_paths_up_to_here = 0
        if 0 <= j - 1:
          unique_paths_up_to_here += unique_paths_to_here[i][j - 1]
        if 0 <= i - 1:
          unique_paths_up_to_here += unique_paths_to_here[i - 1][j]

        unique_paths_to_here[i][j] = unique_paths_up_to_here

    return unique_paths_to_here[-1][-1]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_leetcode_example_1(self):
    m = 3
    n = 2

    expected = 3
    actual = self.solution.uniquePaths(m, n)

    assert actual == expected

  def test_leetcode_example_2(self):
    m = 7
    n = 3

    expected = 28
    actual = self.solution.uniquePaths(m, n)

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
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
