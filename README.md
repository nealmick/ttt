# Tic Tac Toe!
#### But you never win.

The board state is stored using a 3 x 3 array.  Each array index contains an integer of -1, 0, or 1, depending on board state X, empty, or O.  When a move is played the board is converted to a 9 character string representing the board and is then sent to the server.  The server receives the board string and converts the board back to an array.  The server then iterates through all possible board states.  This is done one at a time, recursively until there are no more possible moves.  Each final position is evaluated based on the winner and scored 1 0 -1.  The score is then compared to the best score found so far and updated if necessary.  Once all moves have been evaluated the best move is played and the board state is sent back to the front end.

#### Django apps:
1.  Mysite - Default django app.
2.  ttt - Logic for receiving board states, move generation, and returning board state.

Live:
https://nealmick.com/tictactoe/

Install:
'''
git clone github.com/nealmick/ttt
pip install -r requirements.txt
python3 manage.py runserver
'''
