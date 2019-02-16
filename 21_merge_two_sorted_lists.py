# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __eq__(self, other):
    return self.next == other.next if self.val == other.val else False


class Solution:
  def mergeTwoLists(self, l1, l2):
    n1, n2 = l1, l2

    prev = None
    head = None

    while n1 and n2:
      if n1.val < n2.val:
        next_val = n1.val
        n1 = n1.next
      else:
        next_val = n2.val
        n2 = n2.next

      cur = ListNode(next_val)
      if prev:
        prev.next = cur
      else:
        head = cur

      prev = cur

    while n1:
      cur = ListNode(n1.val)
      if prev:
        prev.next = cur
      else:
        head = cur

      prev = cur
      n1 = n1.next

    while n2:
      cur = ListNode(n2.val)
      if prev:
        prev.next = cur
      else:
        head = cur

      prev = cur
      n2 = n2.next

    return head



class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_numbers(self):
    l1 = None
    l2 = None

    expected = None
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_no_numbers_in_l1(self):
    l1 = None
    l2 = ListNode(1)

    expected = ListNode(1)
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_no_numbers_in_l2(self):
    l1 = ListNode(1)
    l2 = None

    expected = ListNode(1)
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_smaller_number_in_l1(self):
    l1 = ListNode(1)
    l2 = ListNode(2)

    expected = ListNode(1)
    expected.next = ListNode(2)
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_smaller_number_in_l2(self):
    l1 = ListNode(2)
    l2 = ListNode(1)

    expected = ListNode(1)
    expected.next = ListNode(2)
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_l1_smaller_than_l2(self):
    l1 = ListNode(2)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    expected = ListNode(1)
    expected.next = ListNode(2)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(4)
    actual = self.solution.mergeTwoLists(l1, l2)

    assert actual == expected

  def test_l2_smaller_than_l1(self):
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l2 = ListNode(2)

    expected = ListNode(1)
    expected.next = ListNode(2)
    expected.next.next = ListNode(3)
    expected.next.next.next = ListNode(4)
    actual = self.solution.mergeTwoLists(l1, l2)

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
    self.run_test(self.test_no_numbers, 'test_no_numbers')
    self.run_test(self.test_no_numbers_in_l1, 'test_no_numbers_in_l1')
    self.run_test(self.test_no_numbers_in_l2, 'test_no_numbers_in_l2')
    self.run_test(self.test_smaller_number_in_l1, 'test_smaller_number_in_l1')
    self.run_test(self.test_smaller_number_in_l2, 'test_smaller_number_in_l2')
    self.run_test(self.test_l1_smaller_than_l2, 'test_l1_smaller_than_l2')
    self.run_test(self.test_l2_smaller_than_l1, 'test_l2_smaller_than_l1')


tester = TestSolution()
tester.run_tests()
