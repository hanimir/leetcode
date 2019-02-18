class Solution:
  def lengthOfLastWord(self, s):
    words = s.split()
    return len(words[-1]) if len(words) > 0 else 0

class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_words(self):
    s = ''

    expected = 0
    actual = self.solution.lengthOfLastWord(s)

    assert actual == expected

  def test_one_word(self):
    s = 'hello'

    expected = 5
    actual = self.solution.lengthOfLastWord(s)

    assert actual == expected

  def test_many_words(self):
    s = 'hello world this is a sentence'

    expected = 8
    actual = self.solution.lengthOfLastWord(s)

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
    self.run_test(self.test_no_words, 'test_no_words')
    self.run_test(self.test_one_word, 'test_one_word')
    self.run_test(self.test_many_words, 'test_many_words')


tester = TestSolution()
tester.run_tests()
