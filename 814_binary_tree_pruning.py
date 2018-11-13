# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  
  @staticmethod
  def areEqual(root1, root2):
    if root1 == root2 == None:
      return True
    elif root1 == None or root2 == None:
      return False
    
    return root1.val == root2.val and TreeNode.areEqual(root1.left, root2.left) and TreeNode.areEqual(root1.right, root2.right)

class Solution:
  
  def test_one_node_zero(self):
    print('Running test_one_node_zero...')

    root = TreeNode(0)
    expected = None
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_one_node_zero')
    else:
      print('Passed test_one_node_zero!')

  def test_one_node_one(self):
    print('Running test_one_node_one...')

    root = TreeNode(1)
    expected = TreeNode(1)
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_one_node_one')
    else:
      print('Passed test_one_node_one!')

  def test_delete_leaf(self):
    print('Running test_delete_leaf...')

    root = TreeNode(1)
    root.left = TreeNode(0)
    expected = TreeNode(1)
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_delete_leaf')
    else:
      print('Passed test_delete_leaf!')
  
  def test_delete_entire_subtree(self):
    print('Running test_delete_entire_subtree...')

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.right = TreeNode(0)
    expected = TreeNode(1)
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_delete_entire_subtree')
    else:
      print('Passed test_delete_entire_subtree!')
  
  def test_delete_both_subtrees(self):
    print('Running test_delete_both_subtrees...')

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    expected = TreeNode(1)
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_delete_both_subtrees')
    else:
      print('Passed test_delete_both_subtrees!')
  
  def test_keep_subtree(self):
    print('Running test_keep_subtree...')

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.left.right.right = TreeNode(0)
    expected = TreeNode(1)
    expected.left = TreeNode(0)
    expected.left.right = TreeNode(1)
    actual = self.pruneTree(root)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_keep_subtree')
    else:
      print('Passed test_keep_subtree!')
  
  def run_tests(self):
    self.test_one_node_zero()
    self.test_one_node_one()
    self.test_delete_leaf()
    self.test_delete_entire_subtree()
    self.test_delete_both_subtrees()
    self.test_keep_subtree()
  
  def pruneTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root == None:
      return
    
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)

    if root.val == 0 and root.left == None and root.right == None:
      return

    return root

soln = Solution()
soln.run_tests()
