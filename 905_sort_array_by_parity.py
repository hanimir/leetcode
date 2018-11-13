from collections import deque

class Solution:
  def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    sorted_nums = deque()
    for num in A:
      if num % 2 == 0:
        sorted_nums.appendleft(num)
      else:
        sorted_nums.append(num)
    
    return list(sorted_nums)

class SolutionTester:

  def __init__(self):
    self.setup()
  
  def setup(self):
    self.solution = Solution()
  
  def test_two_numbers(self):
    A = [1, 2]
    expected = [2, 1]
    actual = self.solution.sortArrayByParity(A)

    assert(sorted(actual) == sorted(expected))
  
  def test_all_even(self):
    A = [2, 4, 6]
    expected = [6, 4, 2]
    actual = self.solution.sortArrayByParity(A)

    assert(sorted(actual) == sorted(expected))
  
  def run_test(self, test, test_name):
    self.setup()

    print('Running {0}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {0}'.format(test_name))
    else:
      print('Passed {0}'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_two_numbers, 'test_two_numbers')
    self.run_test(self.test_all_even, 'test_all_even')

solution_tester = SolutionTester()
solution_tester.run_tests()