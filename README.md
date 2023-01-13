# Tic Tac Toe#
#### But you never win, checks all possible board states, and might beat you

The algorithm works by finding the next move leading to the desired outcome. The board state is stored using a 3 x 3 array. The algorithm traverses and evaluates a tree structure which contains every possible board state. The root of the tree is the current game state. Each branch of the tree is a possible move. Every level of depth in the tree the player flips. Eventually the branch terminates when the board is full. Each terminal branch is scored on the winner -1, 0, or 1. The best score is kept and updated if a higher scoring branch is found. Once every branch is evaluated the state with the best move is converted back to a 9 character string and sent to the front end. All tree computation takes place on the server. The algorithm is written in Python and uses recursion to iterate through all possible board states. The server is a Django web application.


#### Django apps:
1.  Mysite - Default django app.
2.  ttt - Logic for receiving board states, move generation, and returning board state.
#### Install:

```bash
git clone https://github.com/nealmick/ttt
cd ttt
pip install -r requirements.txt
python3 manage.py runserver
```
Live:
https://nealmick.com/tictactoe/
 

<img src="https://i.imgur.com/gNTOEWa.png" width="300" height="450" />



