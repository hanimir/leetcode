class Solution(object):

  def letter_to_morse(self, letter):
    encoding = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return encoding[ord(letter.lower()) - ord('a')]

  def word_to_morse(self, word):
    return ''.join(self.letter_to_morse(letter) for letter in word)

  def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    unique_morse = set()

    for word in words:
      unique_morse.add(self.word_to_morse(word))

    return len(unique_morse)


class TestSolution:
  def __init__(self):
    self.solution = Solution()

  def test_no_words(self):
    words = []

    expected = 0
    actual = self.solution.uniqueMorseRepresentations(words)

    assert actual == expected

  def test_one_word(self):
    words = ['hello']

    expected = 1
    actual = self.solution.uniqueMorseRepresentations(words)

    assert actual == expected

  def test_many_words(self):
    words = ["gin", "zen", "gig", "msg"]

    expected = 2
    actual = self.solution.uniqueMorseRepresentations(words)

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
