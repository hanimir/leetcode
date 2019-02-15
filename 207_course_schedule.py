class Solution:

  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if numCourses <= 0:
      return False

    if numCourses == 1:
      return True

    start_courses = set([i for i in xrange(numCourses)])
    for [course, _] in prerequisites:
      if course in start_courses:
        start_courses.remove(course)

    sorted_courses = []
    while start_courses:
      course = start_courses.pop()
      sorted_courses.append(course)
      for

    import pdb; pdb.set_trace()

    return False



class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_courses(self):
    numCourses = 0
    prerequisites = []

    expected = False
    actual = self.solution.canFinish(numCourses, prerequisites)

    assert actual == expected

  def test_impossible_to_finish_two_courses(self):
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]

    expected = False
    actual = self.solution.canFinish(numCourses, prerequisites)

    assert actual == expected

  def test_possible_to_finish_two_courses(self):
    numCourses = 2
    prerequisites = [[1, 0]]

    expected = True
    actual = self.solution.canFinish(numCourses, prerequisites)

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
    self.run_test(self.test_no_courses, 'test_no_courses')
    self.run_test(self.test_impossible_to_finish_two_courses, 'test_impossible_to_finish_two_courses')
    self.run_test(self.test_possible_to_finish_two_courses, 'test_possible_to_finish_two_courses')

tester = TestSolution()
tester.run_tests()
