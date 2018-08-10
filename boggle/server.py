from json import dumps
from uuid import uuid4

from flask import Flask

from boggle import Boggle

app = Flask(__name__)

running_games = {}


def create_game():
    return Boggle('../dictionary.txt', '../TestBoard.txt', 3 * 60)


@app.route("/")
def index():
    return dumps(running_games.keys())


@app.route("/new-game")
def new_game():
    uuid = str(uuid4())
    running_games[uuid] = create_game()
    return dumps(uuid)


@app.route("/<id>")
def board(id):
    if id not in running_games:
        return dumps('not a valid game')

    boggle = running_games[id]
    return dumps({
        "board": boggle.board.board,
        "seconds left": boggle.stop_watch.seconds_left(),
        "score": boggle.score
    })


@app.route("/<id>/guess/<guess>")
def guess(id, guess):
    if id not in running_games:
        return dumps('not a valid game')

    boggle = running_games[id]
    return dumps(boggle.take_guess(guess))
