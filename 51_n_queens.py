class Solution:

  def is_valid_location(self, x, y, queens):
    for queen_x, queen_y in queens:
      if x == queen_x or y == queen_y or abs(x - queen_x) == abs(y - queen_y):
        return False

    return True

  def valid_locations_for_next_queen(self, queens, n):
    valid_locations = []
    for i in range(n):
      for j in range(n):
        if self.is_valid_location(i, j, queens):
          valid_locations.append((i, j))

    return valid_locations

  def create_board(self, queens, n):
    board = [['.'] * n for i in range(n)]

    for x, y in queens:
      board[x][y] = 'Q'

    return [''.join(row) for row in board]

  def solveNQueens(self, n):
    states_to_search = [[]]
    solutions = []

    while states_to_search:
      placed_queens = states_to_search.pop()
      if len(placed_queens) == n and sorted(placed_queens) not in solutions:
        solutions.append(sorted(placed_queens))
        continue

      for x, y in self.valid_locations_for_next_queen(placed_queens, n):
        states_to_search.append(placed_queens + [(x, y)])

    return [self.create_board(solution, n) for solution in solutions]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_element(self):
    n = 1

    expected = [['Q']]
    actual = self.solution.solveNQueens(n)

    assert sorted(actual) == sorted(expected)

  def test_leetcode_example(self):
    n = 4

    expected = [
      [".Q..",
        "...Q",
        "Q...",
        "..Q."],
      ["..Q.",
        "Q...",
        "...Q",
        ".Q.."]
    ]
    actual = self.solution.solveNQueens(n)

    assert sorted(actual) == sorted(expected)

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_one_element, 'test_one_element')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
