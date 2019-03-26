from collections import defaultdict


class Solution(object):
  def groupAnagrams(self, strs):
    anagrams = defaultdict(list)
    for word in strs:
      sorted_word = ''.join(sorted(word))
      anagrams[sorted_word].append(word)

    return list(anagrams.values())


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_word(self):
    strs = ['hello']

    expected = [['hello']]
    actual = self.solution.groupAnagrams(strs)

    assert actual == expected

  def test_leetcode_example(self):
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

    expected = [
      ['ate','eat','tea'],
      ['nat','tan'],
      ['bat']]
    actual = self.solution.groupAnagrams(strs)

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
    self.run_test(self.test_one_word, 'test_one_word')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
