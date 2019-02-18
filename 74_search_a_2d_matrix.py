class Solution:
  def searchMatrix(self, matrix, target):
    height = len(matrix)
    if height == 0:
      return False
    width = len(matrix[0])

    left = 0
    right = height * width - 1

    get_coords = lambda i: (i // width, i % width)

    while left <= right:
      middle = (right + left) // 2
      i, j = get_coords(middle)

      if matrix[i][j] == target:
        return True
      elif matrix[i][j] < target:
        left = middle + 1
      else:
        right = middle - 1

    return False


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_number_target_found(self):
    matrix = [[1]]
    target = 1

    expected = True
    actual = self.solution.searchMatrix(matrix, target)

    assert actual == expected

  def test_one_number_target_not_found(self):
    matrix = [[1]]
    target = 2

    expected = False
    actual = self.solution.searchMatrix(matrix, target)

    assert actual == expected

  def test_many_numbers_target_found(self):
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

    target = 6

    expected = True
    actual = self.solution.searchMatrix(matrix, target)

    assert actual == expected

  def test_many_numbers_target_not_found(self):
    matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]
    ]

    target = 15

    expected = False
    actual = self.solution.searchMatrix(matrix, target)

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
    self.run_test(self.test_one_number_target_found, 'test_one_number_target_found')
    self.run_test(self.test_one_number_target_not_found, 'test_one_number_target_not_found')
    self.run_test(self.test_many_numbers_target_found, 'test_many_numbers_target_found')
    self.run_test(self.test_many_numbers_target_not_found, 'test_many_numbers_target_not_found')


tester = TestSolution()
tester.run_tests()
