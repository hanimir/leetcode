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
  def test_leetcode_example(self):
    print('Running test_leetcode_example...')

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)

    expected = TreeNode(4)
    expected.left = TreeNode(2)
    expected.left.left = TreeNode(1)
    expected.left.right = TreeNode(3)
    expected.right = TreeNode(7)
    expected.right.left = TreeNode(5)

    actual = self.insertIntoBST(root, 5)

    try:
      assert(TreeNode.areEqual(actual, expected))
    except AssertionError as e:
      print('Failed test_leetcode_example')
      raise e
    else:
      print('Passed test_leetcode_example!')
  
  def run_tests(self):
    self.test_leetcode_example()

  def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    prev, cur = None, root
    while cur != None:
      prev = cur
      if val > cur.val:
        cur = cur.right
      elif val < cur.val:
        cur = cur.left
    
    if val < prev.val:
      prev.left = TreeNode(val)
    else:
      prev.right = TreeNode(val)
    return root

soln = Solution()
soln.run_tests()