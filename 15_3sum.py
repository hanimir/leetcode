class Solution(object):
  def test_all_zeroes(self):
    print('Running test_all_zeroes...')
    nums = [0, 0, 0, 0, 0]
    expected = [
      [0, 0, 0]
    ]
    actual = self.threeSum(nums)
    try:
      assert(sorted(expected) == sorted(actual))
    except AssertionError as e:
      print('Failed test_all_zeroes')
      raise e

    print('Passed test_all_zeroes!')
  
  def test_some_numbers(self):
    print('Running test_some_numbers...')
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    actual = self.threeSum(nums)
    try:
      assert(sorted(expected) == sorted(actual))
    except AssertionError as e:
      print('Failed test_some_numbers')
      raise e

    print('Passed test_some_numbers!')
  
  def test_no_input(self):
    print('Running test_no_input...')
    nums = []
    expected = []
    actual = self.threeSum(nums)
    try:
      assert(sorted(expected) == sorted(actual))
    except AssertionError as e:
      print('Failed test_no_input')
      raise e

    print('Passed test_no_input!')
  
  def test_no_solution(self):
    print('Running test_no_solution...')
    nums = [1, 1, 1, 1, 1]
    expected = []
    actual = self.threeSum(nums)
    try:
      assert(sorted(expected) == sorted(actual))
    except AssertionError as e:
      print('Failed test_no_solution')
      raise e

    print('Passed test_no_solution!')

  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = set([])
    
    for i in range(len(nums) - 1):

      num_set = set()
      for j in range(i + 1, len(nums)):
        if -(nums[i] + nums[j]) in num_set:
          results.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
        else:
          num_set.add(nums[j])
    
    return [list(result) for result in results]

soln = Solution()
soln.test_all_zeroes()
soln.test_some_numbers()
soln.test_no_input()
soln.test_no_solution()