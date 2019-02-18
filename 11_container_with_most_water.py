class Solution:
  def maxArea(self, height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
      if height[left] < height[right]:
        max_area = max(max_area, height[left] * (right - left))
        left += 1
      else:
        max_area = max(max_area, height[right] * (right - left))
        right -= 1

    return max_area


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_two_lines_smaller_first(self):
    height = [1, 2]

    expected = 1
    actual = self.solution.maxArea(height)

    assert actual == expected

  def test_two_lines_smaller_second(self):
    height = [2, 1]

    expected = 1
    actual = self.solution.maxArea(height)

    assert actual == expected

  def test_cup(self):
    height = [3, 2, 1, 2, 3]

    expected = 12
    actual = self.solution.maxArea(height)

    assert actual == expected

  def test_upside_down_cup(self):
    height = [1, 2, 3, 4, 3, 2, 1]

    expected = 8
    actual = self.solution.maxArea(height)

    assert actual == expected

  def test_cup_with_large_line_in_middle(self):
    height = [3, 2, 1, 10, 1, 2, 3]

    expected = 18
    actual = self.solution.maxArea(height)

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
    self.run_test(self.test_two_lines_smaller_first, 'test_two_lines_smaller_first')
    self.run_test(self.test_two_lines_smaller_second, 'test_two_lines_smaller_second')
    self.run_test(self.test_cup, 'test_cup')
    self.run_test(self.test_upside_down_cup, 'test_upside_down_cup')
    self.run_test(self.test_cup_with_large_line_in_middle, 'test_cup_with_large_line_in_middle')


tester = TestSolution()
tester.run_tests()
