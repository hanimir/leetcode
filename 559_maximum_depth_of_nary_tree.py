# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
  def maxDepth(self, root):
    """
    :type root: Node
    :rtype: int
    """
    if root == None:
      return 0

    return 1 + max(list(map(self.maxDepth, root.children)) + [0])

class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_tree(self):
    root = None

    expected = 0
    actual = self.solution.maxDepth(root)

    assert actual == expected
  
  def test_one_node(self):
    root = Node(1, [])

    expected = 1
    actual = self.solution.maxDepth(root)

    assert actual == expected
  
  def test_small_tree(self):
    child = Node(2, [])
    root = Node(1, [child])

    expected = 2
    actual = self.solution.maxDepth(root)

    assert actual == expected
  
  def test_large_tree(self):
    grandchild = Node(3, [])
    child = Node(2, [grandchild])
    root = Node(1, [child])

    expected = 3
    actual = self.solution.maxDepth(root)

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
    self.run_test(self.test_small_tree, 'test_small_tree')
    self.run_test(self.test_large_tree, 'test_large_tree')


tester = TestSolution()
tester.run_tests()