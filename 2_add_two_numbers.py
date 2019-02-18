# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def __eq__(self, other):
    return self.next == other.next if self.val == other.val else False


class Solution:
  def addTwoNumbers(self, l1, l2):
    n1 = l1
    n2 = l2
    prev = None
    head = None
    carry = 0

    while n1.next or n2.next or n1.val or n2.val:
      res = n1.val + n2.val + carry
      carry = res // 10
      new_val = res % 10

      if n1.next is None:
        n1.next = ListNode(0)

      if n2.next is None:
        n2.next = ListNode(0)

      if head is None:
        head = ListNode(new_val)
        prev = head
      else:
        prev.next = ListNode(new_val)
        prev = prev.next

      n1 = n1.next
      n2 = n2.next

    if carry:
      prev.next = ListNode(carry)

    return head or ListNode(0)



class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_both_zero(self):
    l1 = ListNode(0)
    l2 = ListNode(0)

    expected = ListNode(0)
    actual = self.solution.addTwoNumbers(l1, l2)

    assert actual == expected

  def test_both_single_digit(self):
    l1 = ListNode(1)
    l2 = ListNode(3)

    expected = ListNode(4)
    actual = self.solution.addTwoNumbers(l1, l2)

    assert actual == expected

  def test_carry(self):
    l1 = ListNode(9)
    l2 = ListNode(9)

    expected = ListNode(8)
    expected.next = ListNode(1)
    actual = self.solution.addTwoNumbers(l1, l2)

    assert actual == expected

  def test_multiple_digits(self):
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)

    expected = ListNode(8)
    expected.next = ListNode(9)
    expected.next.next = ListNode(1)
    actual = self.solution.addTwoNumbers(l1, l2)

    assert actual == expected

  def test_different_lengths(self):
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l2 = ListNode(1)

    expected = ListNode(0)
    expected.next = ListNode(0)
    expected.next.next = ListNode(1)
    actual = self.solution.addTwoNumbers(l1, l2)

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
    self.run_test(self.test_both_zero, 'test_both_zero')
    self.run_test(self.test_both_single_digit, 'test_both_single_digit')
    self.run_test(self.test_carry, 'test_carry')
    self.run_test(self.test_multiple_digits, 'test_multiple_digits')
    self.run_test(self.test_different_lengths, 'test_different_lengths')


tester = TestSolution()
tester.run_tests()
