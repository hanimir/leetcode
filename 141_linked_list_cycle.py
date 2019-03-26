# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
  def hasCycle(self, head):
    if not head:
      return False

    node = head
    runner = head.next
    while runner:
      if node == runner:
        return True

      node = node.next
      runner = runner.next
      if runner:
        runner = runner.next

    return False


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_node(self):
    head = ListNode(1)

    expected = False
    actual = self.solution.hasCycle(head)

    assert actual == expected

  def test_no_cycle(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    expected = False
    actual = self.solution.hasCycle(head)

    assert actual == expected

  def test_even_cycle(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next

    expected = True
    actual = self.solution.hasCycle(head)

    assert actual == expected

  def test_odd_cycle(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next

    expected = True
    actual = self.solution.hasCycle(head)

    assert actual == expected

  def test_leetcode_example_1(self):
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    expected = True
    actual = self.solution.hasCycle(head)

    assert actual == expected

  def test_leetcode_example_2(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    expected = True
    actual = self.solution.hasCycle(head)

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
    self.run_test(self.test_no_cycle, 'test_no_cycle')
    self.run_test(self.test_even_cycle, 'test_even_cycle')
    self.run_test(self.test_odd_cycle, 'test_odd_cycle')
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')


tester = TestSolution()
tester.run_tests()
