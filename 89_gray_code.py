class Solution:
  def grayCode(self, n):
    if n == 0:
      return [0]

    codes = [None] * n
    codes[0] = ['0', '1']

    for i in range(1, n):
      prev_code = codes[i - 1]
      prev_code_reversed = reversed(prev_code)
      new_code = ['0' + code for code in prev_code]
      new_code_reversed = ['1' + code for code in prev_code_reversed]
      codes[i] = new_code + new_code_reversed

    return [int(code, 2) for code in codes[-1]]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_zero_bits(self):
    n = 0

    expected = [0]
    actual = self.solution.grayCode(n)

    assert actual == expected

  def test_one_bit(self):
    n = 1

    expected = [0, 1]
    actual = self.solution.grayCode(n)

    assert actual == expected

  def test_two_bits(self):
    n = 2

    expected = [0, 1, 3, 2]
    actual = self.solution.grayCode(n)

    assert actual == expected

  def test_three_bits(self):
    n = 3

    expected = [0, 1, 3, 2, 6, 7, 5, 4]
    actual = self.solution.grayCode(n)

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
    self.run_test(self.test_zero_bits, 'test_zero_bits')
    self.run_test(self.test_one_bit, 'test_one_bit')
    self.run_test(self.test_two_bits, 'test_two_bits')
    self.run_test(self.test_three_bits, 'test_three_bits')


tester = TestSolution()
tester.run_tests()
