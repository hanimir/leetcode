class Solution:
  def peakIndexInMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    for i, num in enumerate(A):
      if i == len(A) - 1 or A[i + 1] < num:
        return i


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_small_mountain(self):
    A = [1, 2, 1]

    expected = 1
    actual = self.solution.peakIndexInMountainArray(A)

    assert actual == expected
  
  def test_mountain_no_left(self):
    A = [2, 1]

    expected = 0
    actual = self.solution.peakIndexInMountainArray(A)

    assert actual == expected
  
  def test_mountain_no_right(self):
    A = [1, 2]

    expected = 1
    actual = self.solution.peakIndexInMountainArray(A)

    assert actual == expected
  
  def test_large_mountain(self):
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

    expected = 4
    actual = self.solution.peakIndexInMountainArray(A)

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
    self.run_test(self.test_small_mountain, 'test_small_mountain')
    self.run_test(self.test_mountain_no_left, 'test_mountain_no_left')
    self.run_test(self.test_mountain_no_right, 'test_mountain_no_right')
    self.run_test(self.test_large_mountain, 'test_large_mountain')


tester = TestSolution()
tester.run_tests()