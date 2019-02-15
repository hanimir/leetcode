class Solution:
  def reverse(self, x):
    sign = 1
    if x < 0:
      x = -x
      sign = -1

    if x > 2**31 - 1:
      return 0

    result = 0

    while x > 0:
      result = result * 10 + x % 10
      x = x // 10

    if result > 2**31 - 1:
      return 0

    return sign * result


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_zero(self):
    x = 0

    expected = 0
    actual = self.solution.reverse(x)

    assert actual == expected

  def test_single_digit(self):
    x = 5

    expected = 5
    actual = self.solution.reverse(x)

    assert actual == expected

  def test_multiple_digits(self):
    x = 523

    expected = 325
    actual = self.solution.reverse(x)

    assert actual == expected

  def test_single_digit_negative(self):
    x = -5

    expected = -5
    actual = self.solution.reverse(x)

    assert actual == expected

  def test_multiple_digits_negative(self):
    x = -523

    expected = -325
    actual = self.solution.reverse(x)

    assert actual == expected

  def test_number_too_large(self):
    x = 1534236469

    expected = 0
    actual = self.solution.reverse(x)

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
    self.run_test(self.test_number_too_large, 'test_number_too_large')

tester = TestSolution()
tester.run_tests()
