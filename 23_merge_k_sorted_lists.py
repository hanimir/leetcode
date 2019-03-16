from heapq import heappush, heappop


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

    return self.val == lst.val and self.next == lst.next

  def __str__(self):
    if not self: return
    return str(self.val) + ' -> ' + str(self.next)


class Solution:
  def mergeKLists(self, lists):
    ordered_nodes = []

    i = 0
    for start_node in lists:
      if not start_node:
        continue

      heappush(ordered_nodes, (start_node.val, i, start_node))
      i += 1

    merged_list = None
    current_node = None
    while ordered_nodes:
      _, _, node = heappop(ordered_nodes)
      if merged_list:
        current_node.next = ListNode(node.val)
        current_node = current_node.next
      else:
        merged_list = ListNode(node.val)
        current_node = merged_list

      if node.next:
        heappush(ordered_nodes, (node.next.val, i, node.next))

      i += 1

    return merged_list


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_list(self):
    l1 = ListNode(1)
    l1.next = ListNode(2)
    lists = [l1]

    expected = ListNode(1)
    expected.next = ListNode(2)
    actual = self.solution.mergeKLists(lists)

    assert actual == expected

  def test_leetcode_example(self):
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]

    expected = ListNode(1)
    expected.next = ListNode(1)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(3)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next.next = ListNode(5)
    expected.next.next.next.next.next.next.next = ListNode(6)
    actual = self.solution.mergeKLists(lists)

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
    self.run_test(self.test_one_list, 'test_one_list')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
