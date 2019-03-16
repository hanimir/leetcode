class Range:

  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __contains__(self, key):
    return self.start <= key <= self.end


class Solution:

  irregularly_named_numbers = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    15: 'Fifteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    80: 'Eighty',
  }

  suffixes = [
    (Range(10, 19), 'teen'),
    (Range(20, 10**2 - 1), 'ty'),
    (Range(10**2, 10**3 - 1), ' Hundred'),
    (Range(10**3, 10**6 - 1), ' Thousand'),
    (Range(10**6, 10**9 - 1), ' Million'),
    (Range(10**9, 10**12 - 1), ' Billion')]

  def get_range_and_suffix(self, num):
    for range, suffix in self.suffixes:
      if num in range:
        return range, suffix

  def numberToWords(self, num):
    if num in self.irregularly_named_numbers:
      return self.irregularly_named_numbers[num]

    number_in_english = ''

    while num > 0:
      import pdb; pdb.set_trace()
      if num in self.irregularly_named_numbers:
        number_in_english += self.irregularly_named_numbers[num]
        break

      range, suffix = self.get_range_and_suffix(num)
      prefix = num // range.start
      number_in_english += self.numberToWords(prefix) + suffix + ' '

      remainder = num % range.start
      num = remainder

    return number_in_english



class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_zero(self):
    num = 0

    expected = 'Zero'
    actual = self.solution.numberToWords(num)

    assert actual == expected

  def test_one(self):
    num = 1

    expected = 'One'
    actual = self.solution.numberToWords(num)

    assert actual == expected

  def test_double_digits(self):
    num = 10

    expected = 'Ten'
    actual = self.solution.numberToWords(num)

    assert actual == expected

  def test_teen(self):
    num = 17

    expected = 'Seventeen'
    actual = self.solution.numberToWords(num)

    assert actual == expected

  def test_leetcode_example_1(self):
    num = 123

    expected = 'One Hundred Twenty Three'
    actual = self.solution.numberToWords(num)

    assert actual == expected

  def test_leetcode_example_2(self):
    num = 12345

    expected = 'Twelve Thousand Three Hundred Forty Five'
    actual = self.solution.numberToWords(num)

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
    # self.run_test(self.test_zero, 'test_zero')
    # self.run_test(self.test_one, 'test_one')
    # self.run_test(self.test_double_digits, 'test_double_digits')
    # self.run_test(self.test_teen, 'test_teen')
    # self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
