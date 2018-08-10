# Boggle game

Boggle is a word game that is played on a 4x4 board with 16 letter tiles. The
goal is to find as many words as possible given a time constraint. For this
exercise, we are making one modification. Now it is possible for one or more of
the letter tiles to be blank (denoted by *). When a tile is blank, it can be
treated as any other letter. Note that in one game it does not have to be the
same character for each word. For example, if the tiles C, T, and * are
adjacent. The words cot, cat, and cut can all be used.

## Starting the game

### CLI mode

To run a cli game, just run 

```bash
cd boggle/
python3 cli.py
```

### Web server mode

To run a game from a webserver, just run

```bash
cd boggle/
export FLASK_APP=server.py
flask run
```

and visit localhost:5000


### Web server example

```json
GET http://localhost:5000/new-game
"74eb7db8-561e-4c74-8794-37821e49e437"
GET http://localhost:5000/74eb7db8-561e-4c74-8794-37821e49e437
{"score": 0, 
 "board": [["T", "A", "P", "*"], ["E", "A", "K", "S"], ["O", "B", "R", "S"], ["S", "*", "X", "D"]], 
 "seconds left": 154.78843593597412}
GET http://localhost:5000/74eb7db8-561e-4c74-8794-37821e49e437/guess/tape
{"success": "found \"tape\""}
GET http://localhost:5000/74eb7db8-561e-4c74-8794-37821e49e437/guess/tape
{"error": "already found"}
GET http://localhost:5000/74eb7db8-561e-4c74-8794-37821e49e437/guess/nothere
{"error": "not in board"}
GET http://localhost:5000/74eb7db8-561e-4c74-8794-37821e49e437/guess/eak
{"error": "not a word"}
```
