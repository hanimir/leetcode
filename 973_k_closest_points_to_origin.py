import math


class Solution:
  def kClosest(self, points, K):
    if len(points) <= K:
      return points

    euclidean_distance = lambda point: math.sqrt(point[0]**2 + point[1]**2)
    points.sort(key=euclidean_distance)
    return points[:K]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_less_than_k_points(self):
    points = [
      [1, 1]]
    k = 2

    expected = [
      [1, 1]]
    actual = self.solution.kClosest(points, k)

    assert sorted(actual) == sorted(expected)

  def test_leetcode_example_1(self):
    points = [
      [1, 3],
      [-2, 2]]
    k = 1

    expected = [
      [-2, 2]]
    actual = self.solution.kClosest(points, k)

    assert sorted(actual) == sorted(expected)

  def test_leetcode_example_2(self):
    points = [
      [3, 3],
      [5, -1],
      [-2, 4]]
    k = 2

    expected = [
      [3, 3],
      [-2, 4]]
    actual = self.solution.kClosest(points, k)

    assert sorted(actual) == sorted(expected)

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_less_than_k_points, 'test_less_than_k_points')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
