# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __eq__(self, other):
    if self and other:
      return self.val == other.val and self.next == other.next
    elif not self and not other:
      return True
    else:
      return False


class Solution:
  def removeNthFromEnd(self, head, n):
    i = 1
    runner = head
    node = head
    prev = None

    while runner:
      if i <= n:
        i += 1
      else:
        prev = node
        node = node.next

      runner = runner.next

    if node == head:
      head = head.next
    else:
      prev.next = node.next

    return head


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_element(self):
    head = ListNode(0)
    n = 1

    expected = None
    actual = self.solution.removeNthFromEnd(head, n)

    assert actual == expected

  def test_remove_head(self):
    head = ListNode(0)
    head.next = ListNode(1)
    n = 2

    expected = ListNode(1)
    actual = self.solution.removeNthFromEnd(head, n)

    assert actual == expected

  def test_remove_tail(self):
    head = ListNode(0)
    head.next = ListNode(1)
    n = 1

    expected = ListNode(0)
    actual = self.solution.removeNthFromEnd(head, n)

    assert actual == expected

  def test_leetcode_example(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2

    expected = ListNode(1)
    expected.next = ListNode(2)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(5)
    actual = self.solution.removeNthFromEnd(head, n)

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
    self.run_test(self.test_one_element, 'test_one_element')
    self.run_test(self.test_remove_head, 'test_remove_head')
    self.run_test(self.test_remove_tail, 'test_remove_tail')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
