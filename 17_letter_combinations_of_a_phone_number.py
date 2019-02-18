class Solution:
  number_to_letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
  }

  def letterCombinations(self, digits):
    if len(digits) == 0:
      return []

    results = []

    # States will contain the string that has been generated
    # and the remaining digits.
    states_to_search = [('', digits)]
    while states_to_search:
      string, remaining_digits = states_to_search.pop()
      if not remaining_digits:
        results.append(string)
        continue

      for letter in self.number_to_letters[remaining_digits[0]]:
        states_to_search.append((string + letter, remaining_digits[1:]))

    return results


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_digits(self):
    digits = ''

    expected = []
    actual = self.solution.letterCombinations(digits)

    assert sorted(actual) == sorted(expected)

  def test_one_digit(self):
    digits = '2'

    expected = [
      'a',
      'b',
      'c'
    ]
    actual = self.solution.letterCombinations(digits)

    assert sorted(actual) == sorted(expected)

  def test_many_digits(self):
    digits = '23'

    expected = [
      'ad',
      'ae',
      'af',
      'bd',
      'be',
      'bf',
      'cd',
      'ce',
      'cf'
    ]
    actual = self.solution.letterCombinations(digits)

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
    self.run_test(self.test_no_digits, 'test_no_digits')
    self.run_test(self.test_one_digit, 'test_one_digit')
    self.run_test(self.test_many_digits, 'test_many_digits')


tester = TestSolution()
tester.run_tests()
