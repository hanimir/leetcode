class Solution:
  def twoSum(self, nums, target):
    nums_seen = {}

    for i, num in enumerate(nums):
      remainder = target - num
      if remainder in nums_seen:
        return sorted([i, nums_seen[remainder]])

      nums_seen[num] = i

class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_small_list(self):
    nums = [1, 2, 3]
    target = 4

    expected = [0, 2]
    actual = self.solution.twoSum(nums, target)

    assert actual == expected

  def test_large_list(self):
    nums = [2, 7, 11, 15, 20, 22]
    target = 26

    expected = [2, 3]
    actual = self.solution.twoSum(nums, target)

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
    self.run_test(self.test_small_list, 'test_small_list')
    self.run_test(self.test_large_list, 'test_large_list')

tester = TestSolution()
tester.run_tests()
