class Solution:
  def longestCommonPrefix(self, strs):
    prefix = ''

    all_same = lambda letters: all([letter == letters[0] for letter in letters])

    for letters in zip(*strs):
      if all_same(letters):
        prefix += letters[0]
      else:
        return prefix

    return prefix


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_only_one_letter(self):
    x = ['a', 'a', 'a']

    expected = 'a'
    actual = self.solution.longestCommonPrefix(x)

    assert actual == expected

  def test_same_words(self):
    x = ['hello', 'hello', 'hello']

    expected = 'hello'
    actual = self.solution.longestCommonPrefix(x)

    assert actual == expected

  def test_small_prefix(self):
    x = ['hello', 'help', 'held']

    expected = 'hel'
    actual = self.solution.longestCommonPrefix(x)

    assert actual == expected

  def test_full_word_prefix(self):
    x = ['hello', 'hell', 'hellstorm']

    expected = 'hell'
    actual = self.solution.longestCommonPrefix(x)

    assert actual == expected

  def test_no_prefix(self):
    x = ['hello', 'there', 'friend']

    expected = ''
    actual = self.solution.longestCommonPrefix(x)

    assert actual == expected

  def test_leetcode_example(self):
    x = ['aca', 'cba']

    expected = ''
    actual = self.solution.longestCommonPrefix(x)

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
    self.run_test(self.test_only_one_letter, 'test_only_one_letter')
    self.run_test(self.test_same_words, 'test_same_words')
    self.run_test(self.test_small_prefix, 'test_small_prefix')
    self.run_test(self.test_full_word_prefix, 'test_full_word_prefix')
    self.run_test(self.test_no_prefix, 'test_no_prefix')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
