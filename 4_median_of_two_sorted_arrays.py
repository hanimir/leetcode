class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    index1 = index2 = 0

    total_length = len(nums1) + len(nums2)

    if total_length == 1:
      return nums1[0] if len(nums1) == 1 else nums2[0]
    
    for i in range(int(total_length / 2) - 1):
      if index1 >= len(nums1):
        index2 += 1
      elif index2 >= len(nums2):
        index1 += 1
      else:
        if nums1[index1] < nums2[index2]:
          index1 += 1
        else:
          index2 += 1
    
    medians = []
    for i in range(2):
      if index1 >= len(nums1):
        medians.append(nums2[index2])
        index2 += 1
      elif index2 >= len(nums2):
        medians.append(nums1[index1])
        index1 += 1
      else:
        if nums1[index1] < nums2[index2]:
          medians.append(nums1[index1])
          index1 += 1
        else:
          medians.append(nums2[index2])
          index2 += 1

    if total_length % 2 == 0:
      return (medians[0] + medians[1]) / 2.0
    else:
      return medians[1]
    
    
class TestSolution:

  def __init__(self):
    self.solution = Solution()
  
  def test_empty_array(self):
    nums1 = [1, 2, 3]
    nums2 = []

    expected = 2
    actual = self.solution.findMedianSortedArrays(nums1, nums2)

    assert(actual == expected)
  
  def test_small_arrays_odd(self):
    nums1 = [1, 3]
    nums2 = [2]

    expected = 2
    actual = self.solution.findMedianSortedArrays(nums1, nums2)

    assert(actual == expected)
  
  def test_small_arrays_even(self):
    nums1 = [1, 3]
    nums2 = [2, 4]

    expected = 2.5
    actual = self.solution.findMedianSortedArrays(nums1, nums2)

    assert(actual == expected)
  
  def test_large_arrays_odd(self):
    nums1 = [1, 2, 4, 6]
    nums2 = [3, 5, 7]

    expected = 4
    actual = self.solution.findMedianSortedArrays(nums1, nums2)

    assert(actual == expected)
  
  def test_large_arrays_even(self):
    nums1 = [1, 2, 4, 6]
    nums2 = [3, 5, 7, 8]

    expected = 4.5
    actual = self.solution.findMedianSortedArrays(nums1, nums2)

    assert(actual == expected)
  
  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except AssertionError as e:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_empty_array, 'test_empty_array')
    self.run_test(self.test_small_arrays_odd, 'test_small_arrays_odd')
    self.run_test(self.test_small_arrays_even, 'test_small_arrays_even')
    self.run_test(self.test_large_arrays_odd, 'test_large_arrays_odd')
    self.run_test(self.test_large_arrays_even, 'test_large_arrays_even')

tester = TestSolution()
tester.run_tests()
