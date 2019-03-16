import math


class Solution:

  def PredictTheWinner(self, nums):
    known_winners = [[0] * len(nums) for _ in range(len(nums))]

    for start in reversed(range(len(nums))):
      for end in range(start + 1, len(nums)):
        score_if_first_element_taken = nums[start] - known_winners[start + 1][end]
        score_if_last_element_taken = nums[end] - known_winners[start][end - 1]
        known_winners[start][end] = max(score_if_first_element_taken, score_if_last_element_taken)

    return known_winners[0][len(nums) - 1] >= 0


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_number(self):
    nums = [1]

    expected = True
    actual = self.solution.PredictTheWinner(nums)

    assert actual == expected

  def test_player_2_wins(self):
    nums = [1, 10, 1]

    expected = False
    actual = self.solution.PredictTheWinner(nums)

    assert actual == expected

  def test_leetcode_example_1(self):
    nums = [1, 5, 2]

    expected = False
    actual = self.solution.PredictTheWinner(nums)

    assert actual == expected

  def test_leetcode_example_2(self):
    nums = [1, 5, 233, 7]

    expected = True
    actual = self.solution.PredictTheWinner(nums)

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
    self.run_test(self.test_one_number, 'test_one_number')
    self.run_test(self.test_player_2_wins, 'test_player_2_wins')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
