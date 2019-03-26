class TicTacToe(object):

  def __init__(self, n):
    """
    Initialize your data structure here.
    :type n: int
    """
    self.n = n
    self.board = [[0 for i in range(n)] for j in range(n)]
    self.game_over = False

  def _player_filled_row(self, row):
    return all([self.board[row][column] == self.board[row][column + 1] for column in range(self.n - 1)])

  def _player_filled_column(self, column):
    return all([self.board[row][column] == self.board[row + 1][column] for row in range(self.n - 1)])

  def _player_filled_diagonal(self):
    return (
      all([self.board[i][i] == self.board[i + 1][i + 1] for i in range(self.n - 1)]) or
      all([self.board[i][self.n - i] == self.board[i + 1][self.n - (i + 1)] for i in range(self.n - 1)]))

  def _check_win_condition(self):
    return (
      any([self._player_filled_row(row) for row in range(self.n)]) or
      any([self._player_filled_column(column) for column in range(self.n)]) or
      self._player_filled_diagonal())

  def move(self, row, col, player):
    """
    Player {player} makes a move at ({row}, {col}).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins.
    :type row: int
    :type col: int
    :type player: int
    :rtype: int
    """
    if self.game_over:
      return

    self.board[row][col] = player
    self.game_over = self._check_win_condition()


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
# param_1 = obj.move(row,col,player)
