# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def sumNumbers(self, root):
    if root is None:
      return 0

    numbers = []

    states_to_search = [('', root)]
    while states_to_search:
      digits, node = states_to_search.pop()
      digits += str(node.val)
      if node.left is None and node.right is None:
        numbers.append(int(digits))
        continue

      if node.left:
        states_to_search.append((digits, node.left))

      if node.right:
        states_to_search.append((digits, node.right))

    return sum(numbers)


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_tree(self):
    root = None

    expected = 0
    actual = self.solution.sumNumbers(root)

    assert actual == expected

  def test_zero(self):
    root = TreeNode(0)

    expected = 0
    actual = self.solution.sumNumbers(root)

    assert actual == expected

  def test_many_numbers_incomplete_tree(self):
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.left.left = TreeNode(0)
    root.right = TreeNode(9)

    expected = 169
    actual = self.solution.sumNumbers(root)

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
    self.run_test(self.test_no_tree, 'test_no_tree')
    self.run_test(self.test_zero, 'test_zero')
    self.run_test(self.test_many_numbers_incomplete_tree, 'test_many_numbers_incomplete_tree')


tester = TestSolution()
tester.run_tests()
