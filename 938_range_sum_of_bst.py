# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def rangeSumBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    if root == None:
      return 0
    
    sum = 0
    
    nodes_to_search = [root]
    while nodes_to_search:
      node = nodes_to_search.pop()
      if node.val < L:
        if node.right:
          nodes_to_search.append(node.right)
      elif node.val > R:
        if node.left:
          nodes_to_search.append(node.left)
      else:
        sum += node.val
        if node.left:
          nodes_to_search.append(node.left)
        if node.right:
          nodes_to_search.append(node.right)

    return sum


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_nodes(self):
    root = None
    L = 0
    R = 1

    expected = 0
    actual = self.solution.rangeSumBST(root, L, R)

    assert(actual == expected)
  
  def test_one_node(self):
    root = TreeNode(1)
    L = 0
    R = 1

    expected = 1
    actual = self.solution.rangeSumBST(root, L, R)

    assert(actual == expected)
  
  def test_small_tree(self):
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    L = 1
    R = 3

    expected = 6
    actual = self.solution.rangeSumBST(root, L, R)

    assert(actual == expected)
  
  def test_large_tree(self):
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    L = 3
    R = 7

    expected = 25 
    actual = self.solution.rangeSumBST(root, L, R)

    assert(actual == expected)
  
  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_no_nodes, 'test_no_nodes')
    self.run_test(self.test_one_node, 'test_one_node')
    self.run_test(self.test_small_tree, 'test_small_tree')
    self.run_test(self.test_large_tree, 'test_large_tree')


tester = TestSolution()
tester.run_tests()
