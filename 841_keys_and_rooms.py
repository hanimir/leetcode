class Solution(object):
  def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    visited_rooms = [False] * len(rooms)
    used_keys = set()
    rooms_to_visit = [0]

    while rooms_to_visit:
      room = rooms_to_visit.pop()
      visited_rooms[room] = True

      if all(visited_rooms):
        return True

      for key in rooms[room]:
        if (room, key) not in used_keys:
          used_keys.add((room, key))
          rooms_to_visit.append(key)

    return False


class TestSolution:

  def __init__(self):
    self.solution = Solution()

  def test_one_room(self):
    rooms = [[]]

    expected = True
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def test_two_rooms(self):
    rooms = [[1], []]

    expected = True
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def test_no_solution(self):
    rooms = [[2], [2], [0]]

    expected = False
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def test_multiple_keys(self):
    rooms = [[2, 1], [2], [0]]

    expected = True
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def test_lots_of_rooms_with_multiple_keys_no_solution(self):
    rooms = [[1,3],[3,0,1],[2],[0]]

    expected = False
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def test_lots_of_rooms_with_multiple_keys(self):
    rooms = [[1,2],[3,0,1],[2],[0]]

    expected = True
    actual = self.solution.canVisitAllRooms(rooms)

    assert actual == expected

  def run_test(self, test, test_name):
    print('Running {}...'.format(test_name))

    try:
      test()
    except AssertionError:
      print('Failed {}'.format(test_name))
    else:
      print('Passed {}!'.format(test_name))

  def run_tests(self):
    self.run_test(self.test_one_room, 'test_one_room')
    self.run_test(self.test_two_rooms, 'test_two_rooms')
    self.run_test(self.test_no_solution, 'test_no_solution')
    self.run_test(self.test_multiple_keys, 'test_multiple_keys')
    self.run_test(self.test_lots_of_rooms_with_multiple_keys_no_solution, 'test_lots_of_rooms_with_multiple_keys_no_solution')
    self.run_test(self.test_lots_of_rooms_with_multiple_keys, 'test_lots_of_rooms_with_multiple_keys')


tester = TestSolution()
tester.run_tests()
