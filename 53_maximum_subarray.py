import math

class Solution:
  def maxSubArray(self, nums):
    if not nums:
      return 0

    max_so_far = -math.inf
    max_ending_here = 0

    for num in nums:
      max_ending_here = max(max_ending_here + num, num)
      max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_nums(self):
    nums = []

    expected = 0
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_one_negative_num(self):
    nums = [-1]

    expected = -1
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_one_num(self):
    nums = [1]

    expected = 1
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_whole_array(self):
    nums = [1, 2, 3, 4, 5, 6]

    expected = 21
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_middle_of_array(self):
    nums = [-1, 2, 3, 4, 5, -6]

    expected = 14
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_small_negative_in_middle_of_array(self):
    nums = [-1, 2, 3, -1, 4, 5, -6]

    expected = 13
    actual = self.solution.maxSubArray(nums)

    assert actual == expected

  def test_large_negative_in_middle_of_array(self):
    nums = [-1, 2, 3, -10, 4, 5, -6]

    expected = 9
    actual = self.solution.maxSubArray(nums)

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
    self.run_test(self.test_no_nums, 'test_no_nums')
    self.run_test(self.test_one_negative_num, 'test_one_negative_num')
    self.run_test(self.test_one_num, 'test_one_num')
    self.run_test(self.test_whole_array, 'test_whole_array')
    self.run_test(self.test_middle_of_array, 'test_middle_of_array')
    self.run_test(self.test_small_negative_in_middle_of_array, 'test_small_negative_in_middle_of_array')
    self.run_test(self.test_large_negative_in_middle_of_array, 'test_large_negative_in_middle_of_array')


tester = TestSolution()
tester.run_tests()
