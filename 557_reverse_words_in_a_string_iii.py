class Solution(object):
  def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s == '':
      return ''

    return ' '.join([word[::-1] for word in s.split()])

class TestSolution:
  def __init__(self):
    self.solution = Solution()

  def test_no_words(self):
    s = ''

    expected = ''
    actual = self.solution.reverseWords(s)

    assert actual == expected

  def test_one_word(self):
    s = 'hello'

    expected = 'olleh'
    actual = self.solution.reverseWords(s)

    assert actual == expected

  def test_some_words(self):
    s = 'this is a test'

    expected = 'siht si a tset'
    actual = self.solution.reverseWords(s)

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
    self.run_test(self.test_some_words, 'test_some_words')


tester = TestSolution()
tester.run_tests()
