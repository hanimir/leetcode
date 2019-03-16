class Solution:

  def get_position_of_rook(self, board):
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == 'R':
          return (i, j)

  def numRookCaptures(self, board):
    captures = 0

    rook_i, rook_j = self.get_position_of_rook(board)

    i = rook_i
    j = rook_j
    while i < len(board) and board[i][j] != 'B':
      if board[i][j] == 'p':
        captures += 1
        break

      i += 1

    i = rook_i
    while i >= 0 and board[i][j] != 'B':
      if board[i][j] == 'p':
        captures += 1
        break

      i -= 1

    i = rook_i
    while j < len(board[0]) and board[i][j] != 'B':
      if board[i][j] == 'p':
        captures += 1
        break

      j += 1

    j = rook_j
    while j >= 0 and board[i][j] != 'B':
      if board[i][j] == 'p':
        captures += 1
        break

      j -= 1

    return captures


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_captures(self):
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['p', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 'p', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 'R', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 'p', '.', '.', '.', '.', '.']]

    expected = 0
    actual = self.solution.numRookCaptures(board)

    assert actual == expected

  def test_bishop_in_the_way(self):
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['p', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 'p', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 'R', '.', 'B', 'p', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 'p', '.', '.', '.', '.', '.']]

    expected = 0
    actual = self.solution.numRookCaptures(board)

    assert actual == expected

  def test_many_captures(self):
    board = [['.', 'p', '.', '.', '.', '.', '.', '.'],
             ['p', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 'p', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['p', 'R', '.', '.', 'p', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 'p', '.', '.', '.', '.', '.']]

    expected = 3
    actual = self.solution.numRookCaptures(board)

    assert actual == expected

  def test_leetcode_example_1(self):
    board = [['.','.','.','.','.','.','.','.'],
             ['.','.','.','p','.','.','.','.'],
             ['.','.','.','R','.','.','.','p'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','p','.','.','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.']]

    expected = 3
    actual = self.solution.numRookCaptures(board)

    assert actual == expected

  def test_leetcode_example_2(self):
    board = [['.','.','.','.','.','.','.','.'],
             ['.','p','p','p','p','p','.','.'],
             ['.','p','p','B','p','p','.','.'],
             ['.','p','B','R','B','p','.','.'],
             ['.','p','p','B','p','p','.','.'],
             ['.','p','p','p','p','p','.','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','.','.','.','.','.']]

    expected = 0
    actual = self.solution.numRookCaptures(board)

    assert actual == expected

  def test_leetcode_example_3(self):
    board = [['.','.','.','.','.','.','.','.'],
             ['.','.','.','p','.','.','.','.'],
             ['.','.','.','p','.','.','.','.'],
             ['p','p','.','R','.','p','B','.'],
             ['.','.','.','.','.','.','.','.'],
             ['.','.','.','B','.','.','.','.'],
             ['.','.','.','p','.','.','.','.'],
             ['.','.','.','.','.','.','.','.']]

    expected = 3
    actual = self.solution.numRookCaptures(board)

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
    self.run_test(self.test_no_captures, 'test_no_captures')
    self.run_test(self.test_bishop_in_the_way, 'test_bishop_in_the_way')
    self.run_test(self.test_many_captures, 'test_many_captures')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')
    self.run_test(self.test_leetcode_example_3, 'test_leetcode_example_3')


tester = TestSolution()
tester.run_tests()
