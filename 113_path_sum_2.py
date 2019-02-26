# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def pathSum(self, root, sum):
    if not root:
      return []

    is_leaf = lambda node: not node.left and not node.right

    paths = []
    paths_to_search = [([root], root.val)]
    while paths_to_search:
      path, path_sum = paths_to_search.pop()
      current_node = path[-1]

      if path_sum == sum and is_leaf(current_node):
        paths.append([node.val for node in path])
        continue

      if current_node.left:
        paths_to_search.append((path + [current_node.left], path_sum + current_node.left.val))

      if current_node.right:
        paths_to_search.append((path + [current_node.right], path_sum + current_node.right.val))

    return paths


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_node_no_sum(self):
    root = TreeNode(0)
    sum = 1

    expected = []
    actual = self.solution.pathSum(root, sum)

    assert sorted(actual) == sorted(expected)

  def test_one_node(self):
    root = TreeNode(1)
    sum = 1

    expected = [
      [1]
    ]
    actual = self.solution.pathSum(root, sum)

    assert sorted(actual) == sorted(expected)

  def test_many_nodes(self):
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right = TreeNode(2)
    sum = 3

    expected = [
      [1, 1, 1],
      [1, 2]
    ]

    actual = self.solution.pathSum(root, sum)

    assert sorted(actual) == sorted(expected)

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_one_node_no_sum, 'test_one_node_no_sum')
    self.run_test(self.test_one_node, 'test_one_node')
    self.run_test(self.test_many_nodes, 'test_many_nodes')


tester = TestSolution()
tester.run_tests()
