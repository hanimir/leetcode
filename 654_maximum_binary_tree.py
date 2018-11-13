import math

class TreeNode:
  def __init__(self, val):
    self.val = val
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

class Heap:
  def __init__(self, nums):
    self.root = self.build_heap(nums)
  
  def get_index_of_max(self, nums):
    index = 0
    max_num = -math.inf

    for i, n in enumerate(nums):
      if n > max_num:
        index = i
        max_num = n
    
    return index, max_num
  
  def build_heap(self, nums):
    if not nums:
      return
    
    i, val = self.get_index_of_max(nums)
    root = TreeNode(val)
    root.left = self.build_heap(nums[:i])
    root.right = self.build_heap(nums[i + 1:])
    return root

class Solution:

  def test_leetcode_example(self):
    print('Running test_leetcode_example...')
    nums = [3,2,1,6,0,5]
    expected = TreeNode(6)
    expected.left = TreeNode(3)
    expected.right = TreeNode(5)

    actual = self.constructMaximumBinaryTree(nums)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_leetcode_example')
      raise e
    else:
      print('Passed test_leetcode_example!')
  
  def run_tests(self):
    self.test_leetcode_example()

  def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    heap = Heap(nums)
    return heap.root

soln = Solution()
soln.run_tests()