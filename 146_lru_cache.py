class ListNode:

  def __init__(self, val, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    self.current = None

  def append(self, value):
    new_node = ListNode(value, prev=self.tail)

    if self.tail:
      self.tail.next = new_node
    else:
      self.head = new_node

    self.tail = new_node
    self.length += 1

    return new_node

  def append_left(self, value):
    new_node = ListNode(value, next=self.head)

    if self.head:
      self.head.prev = new_node
    else:
      self.tail = new_node

    self.head = new_node
    self.length += 1

    return new_node

  def remove(self, node):
    prev = node.prev
    next = node.next
    if prev:
      prev.next = next
    else:
      self.head = next

    if next:
      next.prev = prev
    else:
      self.tail = prev

    node.prev = node.next = None
    self.length -= 1

  def pop(self):
    if not self.tail:
      raise IndexError('Cannot pop from an empty list!')

    tail = self.tail
    self.remove(tail)
    return tail

  def __str__(self):
    output = '\n'

    node = self.head
    while node:
      output += str(node.val)
      if node == self.head:
        output += 'H'
      elif node == self.tail:
        output += 'T'
      if node.next:
        output += ' <--> '
      node = node.next

    return output


class LRUCache:

  def __init__(self, capacity=10):
    self.capacity = capacity
    self.data = {}
    self.ordered_keys = LinkedList()

  def use_key(self, key):
    if key in self.data and 'node' in self.data[key]:
      node = self.data[key]['node']
      self.ordered_keys.remove(node)
    elif key not in self.data:
      self.data[key] = {}

    new_node = self.ordered_keys.append_left(key)
    self.data[key]['node'] = new_node

  def get(self, key):
    if key not in self.data:
      return -1

    self.use_key(key)
    return self.data[key]['value']

  def put(self, key, value):
    if key not in self.data:
      self.data[key] = {}

    self.data[key]['value'] = value
    self.use_key(key)

    while self.ordered_keys.length > self.capacity:
      node_to_remove = self.ordered_keys.pop()
      del(self.data[node_to_remove.val])

  def __str__(self):
    output = '\n'

    node = self.ordered_keys.head
    while node:
      key = node.val
      value = self.data[key]['value']
      output += '{}: {}\n'.format(key, value)
      node = node.next

    return output


class TestSolution:

  def test_leetcode_example(self):
    cache = LRUCache(2)


    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)
    assert cache.get(2) == -1

    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
