class Solution:
  def generateParenthesis(self, n):
    if n <= 0:
      return []

    # States will contain the string that has been generated so far,
    # the number of open parentheses, and the number of closed parentheses.
    states_to_search = [('', 0, 0)]
    results = []

    while states_to_search:
      string, open_parens, closed_parens = states_to_search.pop()
      if open_parens == closed_parens == n:
        results.append(string)
        continue

      if closed_parens < open_parens:
        states_to_search.append((string + ')', open_parens, closed_parens + 1))

      if open_parens < n:
        states_to_search.append((string + '(', open_parens + 1, closed_parens))

    return sorted(results)


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_parentheses(self):
    n = 0

    expected = []
    actual = self.solution.generateParenthesis(n)

    assert sorted(actual) == sorted(expected)

  def test_one_pair(self):
    n = 1

    expected = [
      '()',
    ]
    actual = self.solution.generateParenthesis(n)

    assert sorted(actual) == sorted(expected)

  def test_many_pairs(self):
    n = 3

    expected = [
      '((()))',
      '(()())',
      '(())()',
      '()(())',
      '()()()',
    ]

    actual = self.solution.generateParenthesis(n)

    assert sorted(actual) == sorted(expected)

  def test_leetcode_example(self):
    n = 4

    expected = [
      '(((())))',
      '((()()))',
      '((())())',
      '((()))()',
      '(()(()))',
      '(()()())',
      '(()())()',
      '(())(())',
      '(())()()',
      '()((()))',
      '()(()())',
      '()(())()',
      '()()(())',
      '()()()()',
    ]

    actual = self.solution.generateParenthesis(n)

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
    self.run_test(self.test_no_parentheses, 'test_no_parentheses')
    self.run_test(self.test_one_pair, 'test_one_pair')
    self.run_test(self.test_many_pairs, 'test_many_pairs')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
