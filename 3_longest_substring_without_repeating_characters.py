class Solution:
  def lengthOfLongestSubstring(self, s):
    substring_length = 0
    left = 0
    right = 0

    while right < len(s):
      if s[right] not in s[left:right]:
        right += 1
      else:
        left += 1

      substring_length = max(substring_length, right - left)

    return substring_length


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_string(self):
    s = ''

    expected = 0
    actual = self.solution.lengthOfLongestSubstring(s)

    assert actual == expected

  def test_one_character(self):
    s = 'a'

    expected = 1
    actual = self.solution.lengthOfLongestSubstring(s)

    assert actual == expected

  def test_whole_string(self):
    s = 'abcdefg'

    expected = 7
    actual = self.solution.lengthOfLongestSubstring(s)

    assert actual == expected

  def test_middle_of_string(self):
    s = 'aabcdefgg'

    expected = 7
    actual = self.solution.lengthOfLongestSubstring(s)

    assert actual == expected

  def test_repeat_in_middle_of_string(self):
    s = 'abccdef'

    expected = 4
    actual = self.solution.lengthOfLongestSubstring(s)

    assert actual == expected

  def test_leetcode_example(self):
    s = 'dvdf'

    expected = 3
    actual = self.solution.lengthOfLongestSubstring(s)

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
    self.run_test(self.test_no_string, 'test_no_string')
    self.run_test(self.test_one_character, 'test_one_character')
    self.run_test(self.test_whole_string, 'test_whole_string')
    self.run_test(self.test_middle_of_string, 'test_middle_of_string')
    self.run_test(self.test_repeat_in_middle_of_string, 'test_repeat_in_middle_of_string')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
