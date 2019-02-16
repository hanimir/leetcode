class Solution:
  def isValid(self, s):
    open_parentheses = []
    opposite_parenthesis = {
      ')': '(',
      ']': '[',
      '}': '{'
    }
    open_parens = opposite_parenthesis.values()

    for paren in s:
      if paren in open_parens:
        open_parentheses.append(paren)
      else:
        if not open_parentheses or open_parentheses[-1] != opposite_parenthesis[paren]:
          return False
        open_parentheses.pop()

    return not open_parentheses


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_parentheses(self):
    s = ''

    expected = True
    actual = self.solution.isValid(s)

    assert actual == expected

  def test_small_valid_string(self):
    s = '()'

    expected = True
    actual = self.solution.isValid(s)

    assert actual == expected

  def test_small_invalid_string(self):
    s = '(}'

    expected = False
    actual = self.solution.isValid(s)

    assert actual == expected

  def test_large_valid_string(self):
    s = '[{}(()()(()))]'

    expected = True
    actual = self.solution.isValid(s)

    assert actual == expected

  def test_large_invalid_string(self):
    s = '(()()(()})'

    expected = False
    actual = self.solution.isValid(s)

    assert actual == expected

  def test_no_closed_parens(self):
    s = '((({['

    expected = False
    actual = self.solution.isValid(s)

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
    self.run_test(self.test_no_parentheses, 'test_no_parentheses')
    self.run_test(self.test_small_valid_string, 'test_small_valid_string')
    self.run_test(self.test_small_invalid_string, 'test_small_invalid_string')
    self.run_test(self.test_large_valid_string, 'test_large_valid_string')
    self.run_test(self.test_large_invalid_string, 'test_large_invalid_string')
    self.run_test(self.test_no_closed_parens, 'test_no_closed_parens')


tester = TestSolution()
tester.run_tests()
