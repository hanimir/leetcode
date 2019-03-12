class Variable:

  def __init__(self, name):
    self.name = name
    self.neighbours = []
    self.value = None

  def __hash__(self):
    return hash(self.name)


class Solution:

  @staticmethod
  def parse_equation(equation):
    return equation[0], equation[3], equation[1:3]

  def equationsPossible(self, equations):
    variables = {}
    not_equal = []

    for equation in equations:
      left, right, operator = self.parse_equation(equation)

      if left not in variables:
        variables[left] = Variable(left)

      if right not in variables:
        variables[right] = Variable(right)

      left_variable = variables[left]
      right_variable = variables[right]

      if operator == '==' and left != right:
        left_variable.neighbours.append(right_variable)
        right_variable.neighbours.append(left_variable)
      elif operator == '!=':
        not_equal.append((left_variable, right_variable))

    colours = range(len(variables.values()))
    variables_to_process = list(zip(colours, variables.values()))
    while variables_to_process:
      value, variable = variables_to_process.pop()
      if variable.value:
        continue

      variable.value = value
      for neighbour in variable.neighbours:
        if not neighbour.value:
          variables_to_process.append((value, neighbour))

    for left, right in not_equal:
      if left.value == right.value:
        return False

    return True


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_equation_equal(self):
    equations = ['a==b']

    expected = True
    actual = self.solution.equationsPossible(equations)

    assert actual == expected

  def test_one_equation_not_equal(self):
    equations = ['a!=b']

    expected = True
    actual = self.solution.equationsPossible(equations)

    assert actual == expected

  def test_not_satisfiable(self):
    equations = ['a!=b',
                 'a==b']

    expected = False
    actual = self.solution.equationsPossible(equations)

    assert actual == expected

  def test_leetcode_example_3(self):
    equations = ['a==b',
                 'b==c',
                 'a==c']

    expected = True
    actual = self.solution.equationsPossible(equations)

    assert actual == expected

  def test_leetcode_example_4(self):
    equations = ['a==b',
                 'b!=c',
                 'c==a']

    expected = False
    actual = self.solution.equationsPossible(equations)

    assert actual == expected

  def test_leetcode_example_5(self):
    equations = ['c==c',
                 'b==d',
                 'x!=z']

    expected = True
    actual = self.solution.equationsPossible(equations)

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
    self.run_test(self.test_one_equation_equal, 'test_one_equation_equal')
    self.run_test(self.test_one_equation_not_equal, 'test_one_equation_not_equal')
    self.run_test(self.test_not_satisfiable, 'test_not_satisfiable')
    self.run_test(self.test_leetcode_example_3, 'test_leetcode_example_3')
    self.run_test(self.test_leetcode_example_4, 'test_leetcode_example_4')
    self.run_test(self.test_leetcode_example_5, 'test_leetcode_example_5')


tester = TestSolution()
tester.run_tests()
