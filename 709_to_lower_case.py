class Solution:
  def toLowerCase(self, str_input):
    """
    :type str: str
    :rtype: str
    """
    letters = list(str_input)

    for i, letter in enumerate(letters):
      if letter.isalpha() and letter.isupper():
        letters[i] = letter.lower()

    return ''.join(letters)

class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_already_lowercase(self):
    s = 'hello'

    expected = 'hello'
    actual = self.solution.toLowerCase(s)

    assert(actual == expected)
  
  def test_all_uppercase(self):
    s = 'HELLO'

    expected = 'hello'
    actual = self.solution.toLowerCase(s)

    assert(actual == expected)

  def test_non_alphanumeric(self):
    s = 'al&phaBET'

    expected = 'al&phabet'
    actual = self.solution.toLowerCase(s)

    assert(actual == expected)
  
  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except AssertionError as e:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_already_lowercase, 'test_already_lowercase')
    self.run_test(self.test_all_uppercase, 'test_all_uppercase')
    self.run_test(self.test_non_alphanumeric, 'test_non_alphanumeric')


tester = TestSolution()
tester.run_tests()
