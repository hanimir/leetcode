class Solution:
  def findJudge(self, N, trust):
    person_trusts = [[] for i in range(N)]
    person_trusted_by = [[] for i in range(N)]

    for truster, trusted in trust:
      person_trusts[truster - 1].append(trusted - 1)
      person_trusted_by[trusted - 1].append(truster - 1)

    for i, people_they_trust in enumerate(person_trusts):
      if not people_they_trust and len(person_trusted_by[i]) == N - 1:
        return i + 1

    return -1


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_leetcode_example_1(self):
    N = 2
    trust = [
      [1, 2]
    ]

    expected = 2
    actual = self.solution.findJudge(N, trust)

    assert actual == expected

  def test_leetcode_example_2(self):
    N = 3
    trust = [
      [1, 3],
      [2, 3]
    ]

    expected = 3
    actual = self.solution.findJudge(N, trust)

    assert actual == expected

  def test_leetcode_example_3(self):
    N = 3
    trust = [
      [1, 3],
      [2, 3],
      [3, 1]
    ]

    expected = -1
    actual = self.solution.findJudge(N, trust)

    assert actual == expected

  def test_leetcode_example_4(self):
    N = 3
    trust = [
      [1, 2],
      [2, 3]
    ]

    expected = -1
    actual = self.solution.findJudge(N, trust)

    assert actual == expected

  def test_leetcode_example_5(self):
    N = 4
    trust = [
      [1,3],
      [1,4],
      [2,3],
      [2,4],
      [4,3]
    ]

    expected = 3
    actual = self.solution.findJudge(N, trust)

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
    self.run_test(self.test_leetcode_example_1, 'test_leetcode_example_1')
    self.run_test(self.test_leetcode_example_2, 'test_leetcode_example_2')
    self.run_test(self.test_leetcode_example_3, 'test_leetcode_example_3')
    self.run_test(self.test_leetcode_example_4, 'test_leetcode_example_4')
    self.run_test(self.test_leetcode_example_5, 'test_leetcode_example_5')


tester = TestSolution()
tester.run_tests()
