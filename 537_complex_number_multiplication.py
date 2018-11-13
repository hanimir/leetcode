class Solution:

  def test_all_zeroes(self):
    print('Running test_all_zeroes...')

    a = '0+0i'
    b = '0+0i'

    expected = '0+0i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_all_zeroes')
    else:
      print('Passed test_all_zeroes!')

  def test_only_real(self):
    print('Running test_only_real...')

    a = '2+0i'
    b = '3+0i'

    expected = '6+0i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_only_real')
    else:
      print('Passed test_only_real!')
  
  def test_only_complex(self):
    print('Running test_only_complex...')

    a = '0+3i'
    b = '0+2i'

    expected = '-6+0i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_only_complex')
    else:
      print('Passed test_only_complex!')
  
  def test_negative_real(self):
    print('Running test_negative_real...')

    a = '-2+0i'
    b = '3+0i'

    expected = '-6+0i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_negative_real')
    else:
      print('Passed test_negative_real!')
  
  def test_negative_complex(self):
    print('Running test_negative_complex...')

    a = '0+-2i'
    b = '0+3i'

    expected = '6+0i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_negative_complex')
    else:
      print('Passed test_negative_complex!')
  
  def test_complex(self):
    print('Running test_complex...')

    a = '-2+3i'
    b = '3+-2i'

    expected = '0+13i'
    actual = self.complexNumberMultiply(a, b)

    try:
      assert(actual == expected)
    except AssertionError as e:
      print('Failed test_complex')
    else:
      print('Passed test_complex!')
    
  
  def run_tests(self):
    self.test_all_zeroes()
    self.test_only_real()
    self.test_only_complex()
    self.test_negative_real()
    self.test_negative_complex()
    self.test_complex()

  def complexNumberMultiply(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a_real, a_complex = a.split('+')
    b_real, b_complex = b.split('+')

    a_real = int(a_real)
    a_complex = int(a_complex[:-1])
    b_real = int(b_real)
    b_complex = int(b_complex[:-1])

    real_result = a_real * b_real - a_complex * b_complex
    complex_result = a_real * b_complex + b_real * a_complex

    return '{0}+{1}i'.format(real_result, complex_result)

soln = Solution()
soln.run_tests()