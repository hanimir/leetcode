import math


class Solution:
  def coinChange(self, coins, amount):
    least_coins_for_amount = [math.inf] * (amount + 1)
    least_coins_for_amount[0] = 0

    for value in range(1, len(least_coins_for_amount)):
      for coin in coins:
        if value >= coin:
          coins_required_for_smaller_amount = least_coins_for_amount[value - coin]
          least_coins_for_amount[value] = min(least_coins_for_amount[value], coins_required_for_smaller_amount + 1)

    num_coins = least_coins_for_amount[-1]
    return num_coins if num_coins <= amount else -1


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_only_pennies(self):
    coins = [1]
    amount = 100

    expected = 100
    actual = self.solution.coinChange(coins, amount)

    assert actual == expected

  def test_not_possible(self):
    coins = [2]
    amount = 101

    expected = -1
    actual = self.solution.coinChange(coins, amount)

    assert actual == expected

  def test_largest_coin_doesnt_work(self):
    coins = [7, 4]
    amount = 12

    expected = 3
    actual = self.solution.coinChange(coins, amount)

    assert actual == expected

  def test_leetcode_example_1(self):
    coins = [1, 2, 5]
    amount = 11

    expected = 3
    actual = self.solution.coinChange(coins, amount)

    assert actual == expected

  def test_leetcode_example_2(self):
    coins = [2]
    amount = 3

    expected = -1
    actual = self.solution.coinChange(coins, amount)

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
    self.run_test(self.test_only_pennies, 'test_only_pennies')
    self.run_test(self.test_not_possible, 'test_not_possible')
    self.run_test(self.test_largest_coin_doesnt_work, 'test_largest_coin_doesnt_work')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
