class Solution:
  def sortColors(self, nums):
    zero_index = 0
    two_index = len(nums) - 1


    while zero_index < len(nums) and nums[zero_index] == 0:
      zero_index += 1

    while two_index > 0 and nums[two_index] == 2:
      two_index -= 1

    i = zero_index
    while zero_index <= i <= two_index:
      if nums[i] == 0:
        nums[i] = nums[zero_index]
        nums[zero_index] = 0
        zero_index += 1
        if i < zero_index:
          i = zero_index
      elif nums[i] == 2:
        nums[i] = nums[two_index]
        nums[two_index] = 2
        two_index -= 1
        if i > two_index:
          i = two_index
      else:
        i += 1


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_of_each(self):
    nums = [2, 0, 1]

    expected = [0, 1, 2]
    self.solution.sortColors(nums)

    assert nums == expected

  def test_many_of_each(self):
    nums = [2, 0, 1, 2, 1, 0, 0, 1, 2]

    expected = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    # import pdb; pdb.set_trace()
    self.solution.sortColors(nums)

    assert nums == expected

  def test_leetcode_example(self):
    nums = [2,0,2,1,1,0]

    expected = [0,0,1,1,2,2]
    self.solution.sortColors(nums)

    assert nums == expected

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_one_of_each, 'test_one_of_each')
    self.run_test(self.test_many_of_each, 'test_many_of_each')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
