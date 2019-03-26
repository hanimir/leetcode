from collections import deque


class Solution(object):

  def is_one_letter_away(self, word1, word2):
    if abs(len(word1) - len(word2)) > 1:
      return False

    found_difference = False
    for l1, l2 in zip(word1, word2):
      if l1 != l2:
        if found_difference:
          return False

        found_difference = True

    return found_difference

  def ladderLength(self, beginWord, endWord, wordList):
    if beginWord == endWord:
      return 0

    wordList.append(beginWord)

    words_one_transformation_away = {}
    for word in wordList:
      words_one_transformation_away[word] = [
        transformed_word for transformed_word in wordList
          if self.is_one_letter_away(word, transformed_word)]

    states_to_search = deque([[beginWord]])
    while states_to_search:
      transformations = states_to_search.pop()
      word = transformations[-1]
      if word == endWord:
        return len(transformations)

      for transformed_word in words_one_transformation_away[word]:
        if transformed_word not in transformations:
          states_to_search.appendleft(transformations + [transformed_word])

    return 0


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_same_word(self):
    beginWord = 'hello'
    endWord = 'hello'
    wordList = ['hello']

    expected = 0
    actual = self.solution.ladderLength(beginWord, endWord, wordList)

    assert actual == expected

  def test_one_transformation(self):
    beginWord = 'hello'
    endWord = 'hella'
    wordList = ['hello', 'hella']

    expected = 2
    actual = self.solution.ladderLength(beginWord, endWord, wordList)

    assert actual == expected

  def test_leetcode_example_1(self):
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    expected = 5
    actual = self.solution.ladderLength(beginWord, endWord, wordList)

    assert actual == expected

  def test_leetcode_example_2(self):
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log']

    expected = 0
    actual = self.solution.ladderLength(beginWord, endWord, wordList)

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
    self.run_test(self.test_same_word, 'test_same_word')
    self.run_test(self.test_one_transformation, 'test_one_transformation')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
