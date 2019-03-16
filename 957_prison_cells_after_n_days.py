class Solution:
  def prisonAfterNDays(self, cells, N):
    known_states = {}
    while N > 0:
      if tuple(cells) in known_states:
        N %= known_states[tuple(cells)] - N

      known_states[tuple(cells)] = N

      if N >= 1:
        cells_after_changes = [int(0 < i < len(cells) - 1 and cells[i - 1] == cells[i + 1]) for i in range(len(cells))]
        cells = cells_after_changes
        N -= 1

    return cells


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_cell(self):
    cells = [1]
    N = 1

    expected = [0]
    actual = self.solution.prisonAfterNDays(cells, N)

    assert actual == expected

  def test_two_cells(self):
    cells = [1, 0]
    N = 1

    expected = [0, 0]
    actual = self.solution.prisonAfterNDays(cells, N)

    assert actual == expected

  def test_three_cells(self):
    cells = [1, 0, 1]
    N = 10

    expected = [0, 1, 0]
    actual = self.solution.prisonAfterNDays(cells, N)

    assert actual == expected

  def test_leetcode_example_1(self):
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7

    expected = [0, 0, 1, 1, 0, 0, 0, 0]
    actual = self.solution.prisonAfterNDays(cells, N)

    assert actual == expected

  def test_leetcode_example_2(self):
    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    N = 1000000000

    expected = [0, 0, 1, 1, 1, 1, 1, 0]
    actual = self.solution.prisonAfterNDays(cells, N)

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
    self.run_test(self.test_one_cell, 'test_one_cell')
    self.run_test(self.test_two_cells, 'test_two_cells')
    self.run_test(self.test_three_cells, 'test_three_cells')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
