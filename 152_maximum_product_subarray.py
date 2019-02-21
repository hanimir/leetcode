class Solution:
  def maxProduct(self, nums):
    if not nums:
      return 0

    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = nums[0]
    for num in nums[1:]:
      if num < 0:
        tmp = max_ending_here
        max_ending_here = min_ending_here
        min_ending_here =  tmp

      max_ending_here = max(max_ending_here * num, num)
      min_ending_here = min(min_ending_here * num, num)
      max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_nums(self):
    nums = []

    expected = 0
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_only_zero(self):
    nums = [0]

    expected = 0
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_one_negative_num(self):
    nums = [-1]

    expected = -1
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_one_num(self):
    nums = [1]

    expected = 1
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_whole_array(self):
    nums = [1, 2, 3]

    expected = 6
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_whole_array_with_two_negatives(self):
    nums = [-1, 2, 3, -4]

    expected = 24
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_zero_in_middle_of_array(self):
    nums = [1, 2, 3, 0, 1, 2, 4]

    expected = 8
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_leetcode_example_1(self):
    nums = [2, 3, -2, 4]

    expected = 6
    actual = self.solution.maxProduct(nums)

    assert actual == expected

  def test_leetcode_example_2(self):
    nums = [-2, 0, -1]

    expected = 0
    actual = self.solution.maxProduct(nums)

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
    self.run_test(self.test_only_zero, 'test_only_zero')
    self.run_test(self.test_one_negative_num, 'test_one_negative_num')
    self.run_test(self.test_one_num, 'test_one_num')
    self.run_test(self.test_whole_array, 'test_whole_array')
    self.run_test(self.test_whole_array_with_two_negatives, 'test_whole_array_with_two_negatives')
    self.run_test(self.test_zero_in_middle_of_array, 'test_zero_in_middle_of_array')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
