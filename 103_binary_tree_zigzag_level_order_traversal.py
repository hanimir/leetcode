# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def zigzagLevelOrder(self, root):
    if not root:
      return []

    result = []
    current_level = [root]
    level = 1

    while current_level:
      next_level = []
      if level % 2 == 0:
        result.append([node.val for node in reversed(current_level)])
      else:
        result.append([node.val for node in current_level])

      for node in current_level:
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)

      current_level = next_level
      level += 1

    return result


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_node(self):
    root = TreeNode(1)

    expected = [[1]]
    actual = self.solution.zigzagLevelOrder(root)

    assert actual == expected

  def test_two_levels(self):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    expected = [
      [3],
      [20, 9],
      [8, 10, 15, 7]]
    actual = self.solution.zigzagLevelOrder(root)

    assert actual == expected

  def test_leetcode_example(self):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    expected = [
      [3],
      [20, 9],
      [15, 7]]
    actual = self.solution.zigzagLevelOrder(root)

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
    self.run_test(self.test_two_levels, 'test_two_levels')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
