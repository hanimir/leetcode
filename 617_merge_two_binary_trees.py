# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  
  def __str__(self):
    s1 = [self.left, self.right]
    s2 = []

    output = '{}'.format(self.val)

    while s1:
      output += '\n' + '\t'.join([str(node.val) for node in s1 if node])
      for node in s1:
        if node:
          s2 += [node.left, node.right]
      s1 = s2
      s2 = []
    
    return output


class Solution:

  def test_two_small_trees(self):
    print('Running test_two_small_trees...')

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.right = TreeNode(2)

    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(7)
    root2.left = TreeNode(1)
    root2.left.right = TreeNode(4)

    expected = TreeNode(3)
    expected.left = TreeNode(4)
    expected.left.left = TreeNode(5)
    expected.left.right = TreeNode(4)
    expected.right = TreeNode(5)
    expected.right.right = TreeNode(7)

    actual = self.mergeTrees(root, root2)

    try:
      assert(str(expected) == str(actual))
    except AssertionError as e:
      print('Failed test_two_small_trees')
      raise e
    else:
      print('Passed test_two_small_trees!')
  
  def run_tests(self):
    self.test_two_small_trees()

  def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 == t2 == None:
      return None

    t3 = TreeNode(0)

    s = [(t1 or TreeNode(0), t2 or TreeNode(0), t3)]
    while s:
      cur1, cur2, cur3 = s.pop()
      cur3.val = cur1.val + cur2.val
      if cur1.left == cur1.right == cur2.left == cur2.right == None:
        continue

      if cur1.left or cur2.left:
        cur3.left = TreeNode(0)
        s.append((cur1.left or TreeNode(0), cur2.left or TreeNode(0), cur3.left))
      
      if cur1.right or cur2.right:
        cur3.right = TreeNode(0)
        s.append((cur1.right or TreeNode(0), cur2.right or TreeNode(0), cur3.right))
    
    return t3

soln = Solution()
soln.run_tests()