class Solution:
  def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    directions = {
      'U': (0, 1),
      'D': (0, -1),
      'R': (1, 0),
      'L': (-1, 0)
    }

    start_x, start_y = 0, 0
    for move in moves:
      (x_move, y_move) = directions[move]
      start_x += x_move
      start_y += y_move
    
    return start_x == start_y == 0

class TestSolution:

  def __init__(self):
    self.solution = Solution()
  
  def test_no_moves(self):
    moves = []
    
    expected = True
    actual = self.solution.judgeCircle(moves)

    assert (actual == expected)

  def test_one_move(self):
    moves = ['U']

    expected = False
    actual = self.solution.judgeCircle(moves)

    assert (actual == expected)
    
  def test_small_circle(self):
    moves = ['U', 'D']

    expected = True
    actual = self.solution.judgeCircle(moves)

    assert (actual == expected)
  
  def test_long_path_no_circle(self):
    moves = ['U', 'D', 'L', 'R', 'U']
    
    expected = False
    actual = self.solution.judgeCircle(moves)

    assert (actual == expected)
  
  def test_long_path_circle(self):
    moves = ['U', 'D', 'L', 'R', 'U', 'R', 'D', 'L']
    
    expected = True
    actual = self.solution.judgeCircle(moves)

    assert (actual == expected)
  
  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_no_moves, 'test_no_moves')
    self.run_test(self.test_one_move, 'test_one_move')
    self.run_test(self.test_small_circle, 'test_small_circle')
    self.run_test(self.test_long_path_no_circle, 'test_long_path_no_circle')
    self.run_test(self.test_long_path_circle, 'test_long_path_circle')


tester = TestSolution()
tester.run_tests()