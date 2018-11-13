class Solution:

  def test_small_numbers(self):
    print('Running test_small_numbers...')
    left = 1
    right = 5
    expected = [1, 2, 3, 4, 5]
    actual = self.selfDividingNumbers(left, right)

    try:
      assert(expected == actual)
    except AssertionError as e:
      print('Failed test_small_numbers')
      raise e
    else:
      print('Passed test_small_numbers')

  def test_bigger_numbers(self):
    print('Running test_bigger_numbers...')
    left = 1
    right = 22
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    actual = self.selfDividingNumbers(left, right)

    try:
      assert(expected == actual)
    except AssertionError as e:
      print('Failed test_bigger_numbers')
      raise e
    else:
      print('Passed test_bigger_numbers')

  def run_tests(self):
    self.test_small_numbers()
    self.test_bigger_numbers()
  
  def is_self_dividing(self, original_number):
    n = original_number
    while n >= 1:
      digit = n % 10
      if digit == 0 or original_number % digit != 0:
        return False
      n = n // 10
    
    return True

  def selfDividingNumbers(self, left, right):
      """
      :type left: int
      :type right: int
      :rtype: List[int]
      """
      self_dividing_numbers = []
      
      for i in range(left, right + 1):
        if self.is_self_dividing(i):
          self_dividing_numbers.append(i)
      
      return self_dividing_numbers


soln = Solution()
soln.run_tests()