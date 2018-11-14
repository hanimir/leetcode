import math

class Solution(object):
  def dailyTemperatures(self, T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    next_day_with_temp = {T[-1]: len(T) - 1}
    days_to_wait = [0] * len(T)
    for i in reversed(range(0, len(T) - 1)):
      min_wait = math.inf
      for higher_temp in range(T[i] + 1, 101):
        if higher_temp in next_day_with_temp:
          min_wait = min(min_wait, next_day_with_temp[higher_temp] - i)

      days_to_wait[i] = min_wait if min_wait < math.inf else 0
      next_day_with_temp[T[i]] = i

    return days_to_wait


class TestSolution:
  def __init__(self):
    self.solution = Solution()

  def test_one_day(self):
    T = [50]

    expected = [0]
    actual = self.solution.dailyTemperatures(T)

    assert actual == expected

  def test_no_warmer_day(self):
    T = [50, 49]

    expected = [0, 0]
    actual = self.solution.dailyTemperatures(T)

    assert actual == expected

  def test_next_day_warmer(self):
    T = [49, 50]

    expected = [1, 0]
    actual = self.solution.dailyTemperatures(T)

    assert actual == expected

  def test_future_day_warmer(self):
    T = [49, 48, 50]

    expected = [2, 1, 0]
    actual = self.solution.dailyTemperatures(T)

    assert actual == expected

  def test_large_example(self):
    T = [80, 73, 74, 75, 71, 69, 72, 76, 73]

    expected = [0, 1, 1, 4, 2, 1, 1, 0, 0]
    actual = self.solution.dailyTemperatures(T)

    assert actual == expected

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except AssertionError:
      print('Failed {}'.format(test_name))
    except:
      raise
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_one_day, 'test_one_day')
    self.run_test(self.test_no_warmer_day, 'test_no_warmer_day')
    self.run_test(self.test_next_day_warmer, 'test_next_day_warmer')
    self.run_test(self.test_future_day_warmer, 'test_future_day_warmer')
    self.run_test(self.test_large_example, 'test_large_example')


tester = TestSolution()
tester.run_tests()
