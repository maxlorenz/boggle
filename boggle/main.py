from dictionary_checker import set_from_file, DICTIONARY_PATH
from game_field import Board
from timer import StopWatch

if __name__ == '__main__':
    checker = set_from_file(DICTIONARY_PATH)
    board = Board()
    s = StopWatch(3 * 60)
    board.read_file('../TestBoard.txt')

    board.print_board()
    s.start()
    guess = input('enter word:')
    while (guess):
        if not board.check_word(guess.upper()):
            print('not in board')
        elif guess not in checker:
            print('not a word')
        else:
            print('found!')

        board.print_board()
        print('{} seconds left'.format(s.seconds_left()))
        guess = input('enter word:')
