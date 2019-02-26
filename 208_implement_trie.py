class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.trie = {}

  def insert(self, word):
    """
    Inserts a word into the trie.
    """
    trie = self.trie

    for i, letter in enumerate(word):
      is_end_of_word = i == len(word) - 1
      if letter not in trie:
        trie[letter] = {'is_end_of_word': is_end_of_word}

      trie = trie[letter]

    trie['is_end_of_word'] = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    """
    trie = self.trie

    for letter in word:
      if letter not in trie:
        return False

      trie = trie[letter]

    return trie['is_end_of_word']

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    trie = self.trie

    for letter in prefix:
      if letter not in trie:
        return False

      trie = trie[letter]

    return True

class TestSolution:

  def test_leetcode_example(self):
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")

    trie.insert("app")
    assert trie.search("app")

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
