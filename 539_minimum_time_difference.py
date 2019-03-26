class Solution(object):

  def parse_time(self, time):
    hours, minutes = time.split(':')

    return int(hours), int(minutes)

  def get_difference(self, time1, time2):
    hours1, minutes1 = self.parse_time(time1)
    hours2, minutes2 = self.parse_time(time2)

    return (abs(hours2 - hours1) % 24) * 60 + abs(minutes2 - minutes1)

  def findMinDifference(self, timePoints):
    timePoints.sort()
    # print(min([self.get_difference(timePoints[i], timePoints[i + 1]) for i in range(-1, len(timePoints) - 1)]))
    # import pdb; pdb.set_trace()
    return min([self.get_difference(timePoints[i], timePoints[i + 1]) for i in range(-1, len(timePoints) - 1)])


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_midnight_crossover(self):
    timePoints = ['23:59', '00:00']

    expected = 1
    actual = self.solution.findMinDifference(timePoints)

    assert actual == expected

  def test_many_times(self):
    timePoints = ['00:10', '10:00', '08:54', '23:00', '01:00', '23:03']

    expected = 3
    actual = self.solution.findMinDifference(timePoints)

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
    self.run_test(self.test_midnight_crossover, 'test_midnight_crossover')
    self.run_test(self.test_many_times, 'test_many_times')


tester = TestSolution()
tester.run_tests()
