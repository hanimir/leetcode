class Solution(object):

  def get_area_of_island(self, i, j):
    x_dir = [-1, 0, 0, 1]
    y_dir = [0, -1, 1, 0]
    area = 0

    positions_to_search = [(i, j)]
    while positions_to_search:
      x, y = positions_to_search.pop()

      if self.grid[x][y] == 1:
        area += 1
        self.grid[x][y] = 0

      for x_change, y_change in zip(x_dir, y_dir):
        new_x = x + x_change
        new_y = y + y_change
        if (0 <= new_x < len(self.grid) and
            0 <= new_y < len(self.grid[0]) and
            self.grid[new_x][new_y] == 1):
          positions_to_search.append((new_x, new_y))

    return area

  def maxAreaOfIsland(self, grid):
    if len(grid) == 0 or len(grid[0]) == 0:
      return 0

    self.grid = grid
    area = 0
    for i in range(len(self.grid)):
      for j in range(len(self.grid[0])):
        if self.grid[i][j] == 1:
          area = max(area, self.get_area_of_island(i, j))

    return area


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_islands(self):
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    expected = 0
    actual = self.solution.maxAreaOfIsland(grid)

    assert actual == expected

  def test_leetcode_example_1(self):
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    expected = 6
    actual = self.solution.maxAreaOfIsland(grid)

    assert actual == expected

  def test_leetcode_example_2(self):
    grid = [[0,0,0,0,0,0,0,0]]

    expected = 0
    actual = self.solution.maxAreaOfIsland(grid)

    assert actual == expected

  def test_leetcode_example_3(self):
    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]]

    expected = 4
    actual = self.solution.maxAreaOfIsland(grid)

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
    self.run_test(self.test_no_islands, 'test_no_islands')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')
    self.run_test(self.test_leetcode_example_3, 'test_leetcode_example_3')


tester = TestSolution()
tester.run_tests()
