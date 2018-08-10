from boggle import Boggle


def show_info(boggle):
    print('{} \t SECONDS LEFT: {} \t SCORE: {}'.format(
        boggle.board, int(boggle.stop_watch.seconds_left()), boggle.score))


if __name__ == '__main__':
    boggle = Boggle('../dictionary.txt', '../TestBoard.txt', 3 * 60)
    show_info(boggle)
    guess = input('enter word:')

    while (guess):
        print(boggle.take_guess(guess))
        show_info(boggle)
        guess = input('enter word:')
