# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def findBottomLeftValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    current_level = [root]
    next_level = []

    while True:
      for node in current_level:
        if node.left:
          next_level.append(node.left)

        if node.right:
          next_level.append(node.right)

      if next_level == []:
        return current_level[0].val

      current_level = next_level
      next_level = []


class TestSolution:
  def __init__(self):
    self.solution = Solution()

  def test_one_node(self):
    root = TreeNode(1)

    expected = 1
    actual = self.solution.findBottomLeftValue(root)

    assert actual == expected

  def test_small_tree(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    expected = 2
    actual = self.solution.findBottomLeftValue(root)

    assert actual == expected

  def test_large_tree(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)

    expected = 4
    actual = self.solution.findBottomLeftValue(root)

    assert actual == expected

  def test_large_tree_in_right_half(self):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    expected = 6
    actual = self.solution.findBottomLeftValue(root)

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
    self.run_test(self.test_one_node, 'test_one_node')
    self.run_test(self.test_small_tree, 'test_small_tree')
    self.run_test(self.test_large_tree, 'test_large_tree')


tester = TestSolution()
tester.run_tests()
