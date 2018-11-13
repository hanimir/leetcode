class Solution:
  def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(sorted(nums)[::2])


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_nums(self):
    nums = []

    expected = 0
    actual = self.solution.arrayPairSum(nums)

    assert actual == expected
  
  def test_small_nums(self):
    nums = [1, 2]

    expected = 1
    actual = self.solution.arrayPairSum(nums)

    assert actual == expected
  
  def test_large_nums(self):
    nums = [1, 4, 5, 2, 3, 9]

    expected = 9
    actual = self.solution.arrayPairSum(nums)

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
    self.run_test(self.test_small_nums, 'test_small_nums')
    self.run_test(self.test_large_nums, 'test_large_nums')


tester = TestSolution()
tester.run_tests()