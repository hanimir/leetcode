class Solution:
  def isPalindrome(self, x):
    return str(x) == str(x)[::-1]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_zero(self):
    x = 0

    expected = True
    actual = self.solution.isPalindrome(x)

    assert actual == expected

  def test_single_digit(self):
    x = 5

    expected = True
    actual = self.solution.isPalindrome(x)

    assert actual == expected

  def test_multiple_digits(self):
    x = 525

    expected = True
    actual = self.solution.isPalindrome(x)

    assert actual == expected

  def test_single_digit_negative(self):
    x = -5

    expected = False
    actual = self.solution.isPalindrome(x)

    assert actual == expected

  def test_multiple_digits_negative(self):
    x = -523

    expected = False
    actual = self.solution.isPalindrome(x)

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
    self.run_test(self.test_zero, 'test_zero')
    self.run_test(self.test_single_digit, 'test_single_digit')
    self.run_test(self.test_multiple_digits, 'test_multiple_digits')
    self.run_test(self.test_single_digit_negative, 'test_single_digit_negative')
    self.run_test(self.test_multiple_digits_negative, 'test_multiple_digits_negative')

tester = TestSolution()
tester.run_tests()
