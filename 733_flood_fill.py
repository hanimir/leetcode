from collections import deque


class Solution:
  def get_neighbours(self, x, y, n, m):
    x_dir = [-1, 0, 0, 1]
    y_dir = [0, -1, 1, 0]
    neighbours = []

    for x_change, y_change in zip(x_dir, y_dir):
      if 0 <= x + x_change < n and 0 <= y + y_change < m:
        neighbours.append((x + x_change, y + y_change))

    return neighbours

  def floodFill(self, image, sr, sc, newColor):
    pixels_to_colour = deque([(sr, sc)])
    source_colour = image[sr][sc]

    while pixels_to_colour:
      x, y = pixels_to_colour.popleft()

      image[x][y] = newColor

      for neighbour_x, neighbour_y in self.get_neighbours(x, y, len(image), len(image[0])):
        if image[neighbour_x][neighbour_y] == source_colour and image[neighbour_x][neighbour_y] != newColor:
          pixels_to_colour.append((neighbour_x, neighbour_y))

    return image


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_pixel(self):
    image = [[1]]
    sr = 0
    sc = 0
    new_colour = 2

    expected = [[2]]
    actual = self.solution.floodFill(image, sr, sc, new_colour)

    assert actual == expected

  def test_leetcode_example(self):
    image = [
      [1,1,1],
      [1,1,0],
      [1,0,1]
    ]
    sr = 1
    sc = 1
    new_colour = 2

    expected = [
      [2,2,2],
      [2,2,0],
      [2,0,1]
    ]
    actual = self.solution.floodFill(image, sr, sc, new_colour)

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
    self.run_test(self.test_one_pixel, 'test_one_pixel')
    self.run_test(self.test_leetcode_example, 'test_leetcode_example')


tester = TestSolution()
tester.run_tests()
