class Solution(object):
  def transpose(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(A) == 0 or len(A[0]) == 0:
      return [[]]
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

class TestSolution:
  def __init__(self):
    self.solution = Solution()

  def test_no_entries(self):
    A = [[]]

    expected = [[]]
    actual = self.solution.transpose(A)

    assert actual == expected

  def test_one_entry(self):
    A = [[1]]

    expected = [[1]]
    actual = self.solution.transpose(A)

    assert actual == expected

  def test_some_entries(self):
    A = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

    expected = [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]]

    actual = self.solution.transpose(A)

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
    self.run_test(self.test_no_entries, 'test_no_entries')
    self.run_test(self.test_one_entry, 'test_one_entry')
    self.run_test(self.test_some_entries, 'test_some_entries')


tester = TestSolution()
tester.run_tests()
