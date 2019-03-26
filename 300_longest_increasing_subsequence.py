class Solution(object):
  def lengthOfLIS(self, nums):
    if not nums:
      return 0

    longest_subsequence_including_element = [0] * len(nums)
    longest_subsequence_including_element[0] = 1

    for i in range(1, len(nums)):
      for j in range(i):
        if nums[j] < nums[i]:
          longest_subsequence_including_element[i] = max(longest_subsequence_including_element[i], longest_subsequence_including_element[j])

      longest_subsequence_including_element[i] += 1

    return max(longest_subsequence_including_element)


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_increasing_nums(self):
    nums = [1, 2, 3, 4, 5, 6, 7]

    expected = 7
    actual = self.solution.lengthOfLIS(nums)

    assert actual == expected

  def test_leetcode_example(self):
    nums = [10,9,2,5,3,7,101,18]

    expected = 4
    actual = self.solution.lengthOfLIS(nums)

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
    self.run_test(self.test_increasing_nums, 'test_increasing_nums')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
