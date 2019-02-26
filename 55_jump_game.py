class Solution:
  def canJump(self, nums):
    can_reach_this_position = [False] * len(nums)
    can_reach_this_position[0] = True

    for i in range(len(nums)):
      for j in range(nums[i] + 1):
        if can_reach_this_position[-1]:
          return True

        if i + j < len(nums):
          can_reach_this_position[i + j] = can_reach_this_position[i]

    return can_reach_this_position[-1]


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_element(self):
    nums = [0]

    expected = True
    actual = self.solution.canJump(nums)

    assert actual == expected

  def test_two_elements_not_possible(self):
    nums = [0, 1]

    expected = False
    actual = self.solution.canJump(nums)

    assert actual == expected

  def test_two_elements_possible(self):
    nums = [1, 1]

    expected = True
    actual = self.solution.canJump(nums)

    assert actual == expected

  def test_leetcode_example_1(self):
    nums = [2,3,1,1,4]

    expected = True
    actual = self.solution.canJump(nums)

    assert actual == expected

  def test_leetcode_example_2(self):
    nums = [3,2,1,0,4]

    expected = False
    actual = self.solution.canJump(nums)

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
    self.run_test(self.test_one_element, 'test_one_element')
    self.run_test(self.test_two_elements_not_possible, 'test_two_elements_not_possible')
    self.run_test(self.test_two_elements_possible, 'test_two_elements_possible')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
