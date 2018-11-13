class Solution:
  def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """

    bits = [0]

    for i in range(1, num + 1):
      if i % 2 == 0:
        bits.append(bits[i // 2])
      else:
        bits.append(bits[i - 1] + 1)

    return bits

class TestSolution:

  def __init__(self):
    self.solution = Solution()
  
  def test_zero(self):
    num = 0
    
    expected = [0]
    actual = self.solution.countBits(num)

    assert actual == expected
  
  def test_one(self):
    num = 1
    
    expected = [0, 1]
    actual = self.solution.countBits(num)

    assert actual == expected
  
  def test_power_of_two(self):
    num = 8
    
    expected = [0, 1, 1, 2, 1, 2, 2, 3, 1]
    actual = self.solution.countBits(num)

    assert actual == expected
  
  def test_prime(self):
    num = 17
    
    expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]
    actual = self.solution.countBits(num)

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
    self.run_test(self.test_zero, 'test_zero')
    self.run_test(self.test_one, 'test_one')
    self.run_test(self.test_power_of_two, 'test_power_of_two')
    self.run_test(self.test_prime, 'test_prime')


tester = TestSolution()
tester.run_tests()