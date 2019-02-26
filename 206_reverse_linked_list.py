# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __eq__(self, other):
    return self.next == other.next if self.val == other.val else False


class Solution:
  def reverseList(self, head):
    node = head
    prev = None

    while node:
      next_node = node.next
      node.next = prev
      prev = node
      node = next_node

    return prev


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_node(self):
    head = ListNode(0)

    expected = ListNode(0)
    actual = self.solution.reverseList(head)

    assert actual == expected

  def test_leetcode_example(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    expected = ListNode(5)
    expected.next = ListNode(4)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(2)
    expected.next.next.next.next = ListNode(1)
    actual = self.solution.reverseList(head)

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
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
