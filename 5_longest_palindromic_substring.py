class Solution:
  def longestPalindrome(self, s):
    if len(s) < 2:
      return s

    is_palindrome = [[i == j for j in range(len(s))] for i in range(len(s))]

    longest_palindrome = s[0]

    for palindrome_length in range(1, len(s)):
      for i in range(len(s) - palindrome_length):
        j = i + palindrome_length

        is_palindrome[i][j] = s[i] == s[j] and (palindrome_length <= 2 or is_palindrome[i + 1][j - 1])
        if is_palindrome[i][j] and j - i + 1 > len(longest_palindrome):
          longest_palindrome = s[i:j + 1]

    return longest_palindrome


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_letter(self):
    height = 'a'

    expected = 'a'
    actual = self.solution.longestPalindrome(height)

    assert actual == expected

  def test_one_letter_repeated(self):
    height = 'aaa'

    expected = 'aaa'
    actual = self.solution.longestPalindrome(height)

    assert actual == expected

  def test_many_different_letters(self):
    height = 'abc'

    expected = 'a'
    actual = self.solution.longestPalindrome(height)

    assert actual == expected

  def test_leetcode_example_1(self):
    height = 'babad'

    expected = 'bab'
    actual = self.solution.longestPalindrome(height)

    assert actual == expected

  def test_leetcode_example_2(self):
    height = 'cbbd'

    expected = 'bb'
    actual = self.solution.longestPalindrome(height)

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
    self.run_test(self.test_one_letter, 'test_one_letter')
    self.run_test(self.test_one_letter_repeated, 'test_one_letter_repeated')
    self.run_test(self.test_many_different_letters, 'test_many_different_letters')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
