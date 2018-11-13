class Solution(object):

  def test_small_numbers_1(self):
    print('Running test_small_numbers_1...')
    x = 1
    y = 4
    expected = 2
    actual = self.hammingDistance(x, y)
    try:
      assert(expected == actual)
    except AssertionError as e:
      print('Failed test_small_numbers_1')
      raise e
    else:
      print('Passed test_small_numbers_1!')

  def test_small_numbers_2(self):
    print('Running test_small_numbers_2...')
    x = 1
    y = 2
    expected = 2
    actual = self.hammingDistance(x, y)
    try:
      assert(expected == actual)
    except AssertionError as e:
      print('Failed test_small_numbers_2')
      import pdb; pdb.set_trace()
      raise e
    else:
      print('Passed test_small_numbers_2!')

  def test_small_numbers_3(self):
    print('Running test_small_numbers_3...')
    x = 1
    y = 0
    expected = 1
    actual = self.hammingDistance(x, y)
    try:
      assert(expected == actual)
    except AssertionError as e:
      print('Failed test_small_numbers_3')
      import pdb; pdb.set_trace()
      raise e
    else:
      print('Passed test_small_numbers_3!')
  
  def run_tests(self):
    self.test_small_numbers_1()
    self.test_small_numbers_2()
    self.test_small_numbers_3()

  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x_bin = format(x, '#034b')
    y_bin = format(y, '#034b')

    distance = 0

    for (x_bit, y_bit) in zip(x_bin, y_bin):
      if x_bit != y_bit:
        distance += 1
    
    return distance

soln = Solution()
soln.run_tests()