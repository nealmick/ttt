# ttt
####Tic Tac Toe!

####But you never win.

The board state is sent to the server after a move is made.  The server then creates a fractal of possible moves.  The fractal is then evaluated using a MiniMax algorithm and the best tree is selected.  The move is then made and the new state is sent back to the front end where the board is updated.
