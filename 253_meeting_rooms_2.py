from heapq import heappush, heappop


# Definition for an interval.
class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e


class Solution:
  def minMeetingRooms(self, intervals):
    if not intervals:
      return 0

    meeting_rooms = []
    intervals.sort(key=lambda x: x.start)

    heappush(meeting_rooms, intervals[0].end)
    for meeting in intervals[1:]:
      if meeting_rooms[0] <= meeting.start:
        heappop(meeting_rooms)

      heappush(meeting_rooms, meeting.end)

    return len(meeting_rooms)


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_meetings(self):
    intervals = []

    expected = 0
    actual = self.solution.minMeetingRooms(intervals)

    assert actual == expected

  def test_one_meeting(self):
    intervals = [Interval(0, 1)]

    expected = 1
    actual = self.solution.minMeetingRooms(intervals)

    assert actual == expected

  def test_leetcode_example_1(self):
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

    expected = 2
    actual = self.solution.minMeetingRooms(intervals)

    assert actual == expected

  def test_leetcode_example_2(self):
    intervals = [Interval(7, 10), Interval(2, 4)]

    expected = 1
    actual = self.solution.minMeetingRooms(intervals)

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
    self.run_test(self.test_no_meetings, 'test_no_meetings')
    self.run_test(self.test_one_meeting, 'test_one_meeting')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
