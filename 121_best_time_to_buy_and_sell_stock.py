import math


class Solution:
  def maxProfit(self, prices):
    if not prices:
      return 0

    max_profit = 0
    min_price = math.inf
    for price in prices:
      min_price = min(min_price, price)
      max_profit = max(max_profit, price - min_price)

    return max_profit


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_days(self):
    prices = []

    expected = 0
    actual = self.solution.maxProfit(prices)

    assert actual == expected

  def test_one_day(self):
    prices = [1]

    expected = 0
    actual = self.solution.maxProfit(prices)

    assert actual == expected

  def test_price_drops(self):
    prices = [10, 1]

    expected = 0
    actual = self.solution.maxProfit(prices)

    assert actual == expected

  def test_price_increases(self):
    prices = [1, 10]

    expected = 9
    actual = self.solution.maxProfit(prices)

    assert actual == expected

  def test_leetcode_example_1(self):
    prices = [7, 1, 5, 3, 6, 4]

    expected = 5
    actual = self.solution.maxProfit(prices)

    assert actual == expected

  def test_leetcode_example_2(self):
    prices = [7, 6, 4, 3, 1]

    expected = 0
    actual = self.solution.maxProfit(prices)

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
    self.run_test(self.test_no_days, 'test_no_days')
    self.run_test(self.test_one_day, 'test_one_day')
    self.run_test(self.test_price_drops, 'test_price_drops')
    self.run_test(self.test_price_increases, 'test_price_increases')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
