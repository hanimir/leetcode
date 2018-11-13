# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:

  def test_even_length(self):
    print('Running test_even_length...')

    lst = ListNode(1)
    lst.next = ListNode(2)
    lst.next.next = ListNode(3)
    lst.next.next.next = ListNode(4)
    lst.next.next.next.next = ListNode(5)

    expected = lst.next.next
    actual = self.middleNode(lst)

    try:
      assert(actual == expected)
    except e:
      print('Failed test_even_length')
      raise e
    else:
      print('Passed test_even_length!')

  def test_odd_length(self):
    print('Running test_odd_length...')

    lst = ListNode(1)
    lst.next = ListNode(2)
    lst.next.next = ListNode(3)
    lst.next.next.next = ListNode(4)
    lst.next.next.next.next = ListNode(5)
    lst.next.next.next.next.next = ListNode(6)

    expected = lst.next.next.next
    actual = self.middleNode(lst)

    try:
      assert(actual == expected)
    except e:
      print('Failed test_odd_length')
      raise e
    else:
      print('Passed test_odd_length!')

  def run_tests(self):
    self.test_even_length()
    self.test_odd_length()
  
  def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

soln = Solution()
soln.run_tests()