import bisect

from collections import deque

class RecentCounter:

  def __init__(self):
    self.times = deque()

  def ping(self, t):
    """
    :type t: int
    :rtype: int
    """
    self.times.append(t)
    while self.times[0] < t - 3000:
      self.times.popleft()
    return len(self.times)

class TestRecentCounter:

  def __init__(self):
    self.setup()
  
  def setup(self):
    self.recentCounter = RecentCounter()
  
  def test_one_ping(self):
    expected = 1
    actual = self.recentCounter.ping(1)

    assert(actual == expected)
  
  def test_two_pings_in_interval(self):
    expected = 2
    self.recentCounter.ping(1)
    actual = self.recentCounter.ping(2)

    assert(actual == expected)
  
  def test_two_pings_not_in_interval(self):
    expected = 1
    self.recentCounter.ping(1)
    actual = self.recentCounter.ping(3002)

    assert(actual == expected)

  def run_test(self, test, test_name):
    self.setup()

    print('Running {0}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {0}'.format(test_name))
    else:
      print('Passed {0}'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_one_ping, 'test_one_ping')
    self.run_test(self.test_two_pings_in_interval, 'test_two_pings_in_interval')
    self.run_test(self.test_two_pings_not_in_interval, 'test_two_pings_not_in_interval')

tester = TestRecentCounter()
tester.run_tests()