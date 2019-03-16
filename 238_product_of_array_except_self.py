class Solution:
  def productExceptSelf(self, nums):
    output = [1] * len(nums)

    left_product = 1
    right_product = 1
    for i in range(len(nums)):
      output[i] *= left_product
      output[-(i + 1)] *= right_product
      left_product *= nums[i]
      right_product *= nums[-(i + 1)]

    return output


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_num(self):
    nums = [1]

    expected = [1]
    actual = self.solution.productExceptSelf(nums)

    assert actual == expected

  def test_leetcode_example(self):
    nums = [1, 2, 3, 4]

    expected = [24, 12, 8, 6]
    actual = self.solution.productExceptSelf(nums)

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
    self.run_test(self.test_one_num, 'test_one_num')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
