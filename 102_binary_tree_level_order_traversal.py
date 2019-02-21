# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def levelOrder(self, root):
    if root is None:
      return []

    levels = []

    current_level = [root]
    next_level = []
    while current_level:
      for node in current_level:
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)

      levels.append([node.val for node in current_level])
      current_level = next_level
      next_level = []

    return levels


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_tree(self):
    root = None

    expected = []
    actual = self.solution.levelOrder(root)

    assert actual == expected

  def test_one_node(self):
    root = TreeNode(1)

    expected = [[1]]
    actual = self.solution.levelOrder(root)

    assert actual == expected

  def test_multiple_levels_full_tree(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    expected = [
      [1],
      [2, 3]
    ]
    actual = self.solution.levelOrder(root)

    assert actual == expected

  def test_multiple_levels_some_missing(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    expected = [
      [1],
      [2, 3],
      [4]
    ]
    actual = self.solution.levelOrder(root)

    assert actual == expected

  def test_leetcode_example(self):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    expected = [
      [3],
      [9, 20],
      [15, 7]
    ]
    actual = self.solution.levelOrder(root)

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
    self.run_test(self.test_one_node, 'test_one_node')
    self.run_test(self.test_multiple_levels_full_tree, 'test_multiple_levels_full_tree')
    self.run_test(self.test_multiple_levels_some_missing, 'test_multiple_levels_some_missing')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
