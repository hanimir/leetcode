class Solution:
  def mark_island(self, i, j):
    x_dir = [-1, 0, 0, 1]
    y_dir = [0, -1, 1, 0]

    points_to_flag = [(i, j)]

    while points_to_flag:
      x, y = points_to_flag.pop()
      self.grid[x][y] = 0

      for x_change, y_change in zip(x_dir, y_dir):
        new_x = x + x_change
        new_y = y + y_change
        if (0 <= new_x < len(self.grid) and
            0 <= new_y < len(self.grid[0]) and
            self.grid[new_x][new_y] == '1'):
          points_to_flag.append((new_x, new_y))

  def numIslands(self, grid):
    self.grid = grid
    islands = 0

    for i in range(len(self.grid)):
      for j in range(len(self.grid[0])):
        if self.grid[i][j] == '1':
          islands += 1
          self.mark_island(i, j)

    return islands


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_leetcode_example_1(self):
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]

    expected = 1
    actual = self.solution.numIslands(grid)

    assert actual == expected

  def test_leetcode_example_2(self):
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]

    expected = 3
    actual = self.solution.numIslands(grid)

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
