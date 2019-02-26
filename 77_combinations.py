import itertools

class Solution:
  def combine(self, n, k):
    if n == 0 or k == 0:
      return [()]

    results = set()

    states_to_search = [([], list(range(1, n + 1)))]
    while states_to_search:
      combination, unused_numbers = states_to_search.pop()
      if len(combination) == k:
        results.add(combination)
        break

      for i, number in enumerate(unused_numbers):
        numbers_before_i = unused_numbers[:i]
        numbers_after_i = unused_numbers[i + 1:]
        states_to_search.append((combination + [number], numbers_before_i + numbers_after_i))

    return sorted(list(results))


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_no_combinations(self):
    n = 0
    k = 0

    expected = itertools.permutations(range(1, n + 1), k)
    actual = self.solution.combine(n, k)

    assert actual == expected

  def test_all_numbers(self):
    n = 4
    k = 4

    expected = itertools.permutations(range(1, n + 1), k)
    actual = self.solution.combine(n, k)

    assert actual == expected

  def test_some_numbers(self):
    n = 4
    k = 3

    expected = itertools.permutations(range(1, n + 1), k)
    actual = self.solution.combine(n, k)

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
    self.run_test(self.test_no_combinations, 'test_no_combinations')
    self.run_test(self.test_all_numbers, 'test_all_numbers')


tester = TestSolution()
tester.run_tests()
