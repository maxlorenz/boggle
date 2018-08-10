def list_to_grid(input_list, grid_size=4):
    grid = []

    while len(input_list) >= grid_size:
        grid.append(input_list[0:grid_size])
        input_list = input_list[grid_size:]

    return grid


def board_from_file(file_path, grid_size=4):
    with open(file_path, 'r') as board_file:
        board_line = board_file.readline()
        fields = board_line.split(', ')
        return list_to_grid(fields, grid_size)


class Board():
    def __init__(self, dictionary_file):
        self.load_file(dictionary_file)

    def __str__(self):
        string = ''
        for row in self.board:
            string += ' '.join(row)
            string += '\n'

        return string

    def load_file(self, file_path):
        self.board = board_from_file(file_path)

    def _board_size(self):
        return len(self.board)

    def _matches(self, letter, board_letter):
        return ((letter.lower() == board_letter.lower())
                or (board_letter == '*'))

    def _find_letter(self, letter):
        pos = [[x, y] for x in range(self._board_size())
               for y in range(self._board_size())]

        for [x, y] in pos:
            board_letter = self.board[x][y]
            if self._matches(letter, board_letter):
                yield (board_letter, x, y)

    def _valid_position(self, x, y):
        return (0 <= x < self._board_size()) and (0 <= y < self._board_size())

    def _get_neighbors(self, board_letter):
        _, x, y = board_letter

        diffs = [[x, y] for x in [-1, 0, 1] for y in [-1, 0, 1]
                 if x != 0 or y != 0]

        for [diff_x, diff_y] in diffs:
            new_x, new_y = x + diff_x, y + diff_y
            if self._valid_position(new_x, new_y):
                yield (self.board[new_x][new_y], new_x, new_y)

    def _check_word(self, start, word):
        if not word:
            return True

        for neighbor in self._get_neighbors(start):
            (letter, _, _) = neighbor
            first_letter, rest = word[0], word[1:]

            if (self._matches(first_letter, letter)
                    and self._check_word(neighbor, rest)):
                return True

        return False

    def check_word(self, word):
        first_letter, rest = word[0], word[1:]

        for possible_start in self._find_letter(first_letter):
            if self._check_word(possible_start, rest):
                return True

        return False
