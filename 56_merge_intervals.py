# Definition for an interval.
class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

  def __eq__(self, interval):
    return self.start == interval.start and self.end == interval.end


class Solution:
  def merge(self, intervals):
    if not intervals:
      return []

    intervals.sort(key=lambda x: x.start)
    merged_intervals = [intervals[0]]
    for interval in intervals[1:]:
      prev_interval = merged_intervals[-1]
      if interval.start <= prev_interval.end:
        prev_interval.end = max(prev_interval.end, interval.end)
      else:
        merged_intervals.append(interval)

    return merged_intervals


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_intervals(self):
    intervals = []

    expected = []
    actual = self.solution.merge(intervals)

    assert actual == expected

  def test_leetcode_example_1(self):
    raw_intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [Interval(start, end) for start, end in raw_intervals]

    raw_expected = [[1,6],[8,10],[15,18]]
    expected = [Interval(start, end) for start, end in raw_expected]
    actual = self.solution.merge(intervals)

    assert actual == expected

  def test_leetcode_example_2(self):
    raw_intervals = [[1,4],[4,5]]
    intervals = [Interval(start, end) for start, end in raw_intervals]

    raw_expected = [[1,5]]
    expected = [Interval(start, end) for start, end in raw_expected]
    actual = self.solution.merge(intervals)

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
    self.run_test(self.test_no_intervals, 'test_no_intervals')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
