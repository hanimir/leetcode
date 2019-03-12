class Solution:
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    reversed_digits = list(reversed(digits))

    carry = 1
    for i, digit in enumerate(reversed_digits):
      new_digit = (digit + carry) % 10
      carry = (digit + carry) // 10
      reversed_digits[i] = new_digit

    if carry:
      reversed_digits.append(carry)

    return list(reversed(reversed_digits))


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_zero(self):
    digits = [0]

    expected = [1]
    actual = self.solution.plusOne(digits)

    assert(actual == expected)

  def test_one(self):
    digits = [1]

    expected = [2]
    actual = self.solution.plusOne(digits)

    assert(actual == expected)

  def test_carry(self):
    digits = [9]

    expected = [1, 0]
    actual = self.solution.plusOne(digits)

    assert(actual == expected)

  def test_carry_multiple_times(self):
    digits = [9, 9, 9]

    expected = [1, 0, 0, 0]
    actual = self.solution.plusOne(digits)

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
    self.run_test(self.test_zero, 'test_zero')
    self.run_test(self.test_one, 'test_one')
    self.run_test(self.test_carry, 'test_carry')
    self.run_test(self.test_carry_multiple_times, 'test_carry_multiple_times')

tester = TestSolution()
tester.run_tests()
