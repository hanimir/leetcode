class Solution:
  def get_neighbours(self, x, y, n, m):
    x_dir = [-1, 0, 0, 1]
    y_dir = [0, -1, 1, 0]

    neighbours = []

    for x_change, y_change in zip(x_dir, y_dir):
      new_x = x + x_change
      new_y = y + y_change
      if 0 <= new_x < n and 0 <= new_y < m:
        neighbours.append((new_x, new_y))

    return neighbours

  def exist(self, board, word):
    paths_to_search = []

    # Initialize possible starting positions.
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == word[0]:
          paths_to_search.append(([(i, j)], 0))

    while paths_to_search:
      path, word_index = paths_to_search.pop()
      if word_index == len(word) - 1:
        return True

      x, y = path[-1]
      for next_x, next_y in self.get_neighbours(x, y, len(board), len(board[0])):
        if (next_x, next_y) not in path and board[next_x][next_y] == word[word_index + 1]:
          paths_to_search.append((path + [(next_x, next_y)], word_index + 1))

    return False


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_letter_true(self):
    board = [['A']]
    word = 'A'

    expected = True
    actual = self.solution.exist(board, word)

    assert actual == expected

  def test_one_letter_false(self):
    board = [['A']]
    word = 'B'

    expected = False
    actual = self.solution.exist(board, word)

    assert actual == expected

  def test_leetcode_example_1(self):
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'ABCCED'

    expected = True
    actual = self.solution.exist(board, word)

    assert actual == expected

  def test_leetcode_example_2(self):
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'SEE'

    expected = True
    actual = self.solution.exist(board, word)

    assert actual == expected

  def test_leetcode_example_3(self):
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = 'ABCB'

    expected = False
    actual = self.solution.exist(board, word)

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
    self.run_test(self.test_one_letter_true, 'test_one_letter_true')
    self.run_test(self.test_one_letter_false, 'test_one_letter_false')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')
    self.run_test(self.test_leetcode_example_3, 'test_leetcode_example_3')


tester = TestSolution()
tester.run_tests()
