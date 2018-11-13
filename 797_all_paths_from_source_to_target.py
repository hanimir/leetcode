class Solution:
  def allPathsSourceTarget(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(graph) - 1
    s = [[0]]
    paths = []
    while s:
      current_path = s.pop()
      current_node = current_path[-1]
      if current_node == n:
        paths.append(current_path)
        continue
      
      for neighbour in graph[current_node]:
        s.append(current_path + [neighbour])
    
    return paths

class SolutionTester:

  def __init__(self):
    self.setup()
  
  def setup(self):
    self.solution = Solution()
  
  def test_two_nodes(self):
    graph = [[1], []]
    expected = [[0, 1]]
    actual = self.solution.allPathsSourceTarget(graph)

    assert(sorted(actual) == sorted(expected))

  def test_leetcode_example(self):
    graph = [[1,2], [3], [3], []]
    expected = [[0,1,3], [0,2,3]]
    actual = self.solution.allPathsSourceTarget(graph)

    assert(sorted(actual) == sorted(expected))
  
  def run_test(self, test, test_name):
    self.setup()

    print('Running {0}...'.format(test_name))

    try:
      test()
    except:
      print('Failed {0}'.format(test_name))
    else:
      print('Passed {0}'.format(test_name))
  
  def run_tests(self):
    self.run_test(self.test_two_nodes, 'test_two_nodes')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')

solution_tester = SolutionTester()
solution_tester.run_tests()