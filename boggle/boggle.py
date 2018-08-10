from dictionary_checker import set_from_file
from board import Board
from timer import StopWatch


class Boggle(object):
    def __init__(self, dictionary_file, board_file, seconds):
        self.checker = set_from_file(dictionary_file)
        self.board = Board(board_file)
        self.stop_watch = StopWatch(seconds)
        self.score = 0
        self.found_words = set()
        self.stop_watch.start()

    def take_guess(self, guess):
        if not self.stop_watch.check():
            return {'error': 'time is up'}

        elif not self.board.check_word(guess):
            return {'error': 'not in board'}

        elif guess not in self.checker:
            return {'error': 'not a word'}

        elif guess in self.found_words:
            return {'error': 'already found'}

        self.score += len(guess)
        self.found_words.add(guess)
        return {'success': 'found "{}"'.format(guess)}
