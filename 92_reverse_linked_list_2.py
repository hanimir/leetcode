# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __eq__(self, lst):
    if not self and not lst:
      return True

    if not all([self, lst]):
      return False

    return self.next == lst.next if self.val == lst.val else False

  def __str__(self):
    if not self: return
    return str(self.val) + ' -> ' + str(self.next)


class Solution:
  def reverseBetween(self, head, m, n):
    i = 1
    current = head
    prev = None
    next = None
    end_of_reversed_list = None

    while i <= n:
      next = current.next

      if i == m:
        end_of_reversed_list = current

      if i >= m:
        current.next = prev

      prev = current
      current = next
      i += 1

    node_before_reversed_list = end_of_reversed_list.next
    if node_before_reversed_list:
      node_before_reversed_list.next = prev
    else:
      head = prev

    end_of_reversed_list.next = current

    return head


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_node(self):
    head = ListNode(0)
    m = 1
    n = 1

    expected = ListNode(0)
    actual = self.solution.reverseBetween(head, m, n)

    assert actual == expected

  def test_two_nodes(self):
    head = ListNode(3)
    head.next = ListNode(5)
    m = 1
    n = 2

    expected = ListNode(5)
    expected.next = ListNode(3)
    actual = self.solution.reverseBetween(head, m, n)

    assert actual == expected

  def test_reverse_head(self):
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(7)
    m = 1
    n = 2

    expected = ListNode(5)
    expected.next = ListNode(3)
    expected.next.next = ListNode(7)
    actual = self.solution.reverseBetween(head, m, n)

    assert actual == expected

  def test_reverse_tail(self):
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(7)
    m = 2
    n = 3

    expected = ListNode(3)
    expected.next = ListNode(7)
    expected.next.next = ListNode(5)
    actual = self.solution.reverseBetween(head, m, n)

    assert actual == expected

  def test_leetcode_example(self):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    m = 2
    n = 4

    expected = ListNode(1)
    expected.next = ListNode(4)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(2)
    expected.next.next.next.next = ListNode(5)
    actual = self.solution.reverseBetween(head, m, n)

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
    self.run_test(self.test_two_nodes, 'test_two_nodes')
    self.run_test(self.test_reverse_head, 'test_reverse_head')
    self.run_test(self.test_reverse_tail, 'test_reverse_tail')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
