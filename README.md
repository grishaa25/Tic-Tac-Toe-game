# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game that allows two players to play over a network. It consists of three components:
1. **Server**: Acts as the game coordinator, handling the connection between Player 1 and Player 2.
2. **Player 1**: Connects to the server and plays as 'X'.
3. **Player 2**: Connects to the server and plays as 'O'.

## Requirements
- Python 3.x
- `socket` library (included in Python's standard library)

## How to Run
### Step 1: Start the Server
1. Open a terminal.
2. Navigate to the directory where the server code is located.
3. Run the following command to start the server:
The server will wait for Player 1 and Player 2 to connect.

### Step 2: Start Player 1
1. Open another terminal.
2. Navigate to the directory where the Player 1 code is located.
3. Run the following command to start Player 1:
4. Player 1 will connect to the server and play as 'X'.

### Step 3: Start Player 2
1. Open another terminal.
2. Navigate to the directory where the Player 2 code is located.
3. Run the following command to start Player 2:
4. Player 2 will connect to the server and play as 'O'.

### Step 4: Play the Game
- Player 1 and Player 2 will take turns to mark a cell on the board.
- The game ends when either one player wins or the board is full and the game results in a draw.

## How It Works
- **Server**: The server listens for incoming connections on a specific port. Once both players are connected, it alternates between Player 1 and Player 2 to update the game board and check for a winner.
- **Player 1**: Connects to the server and plays as 'X'. Player 1 makes their move by entering the row and column numbers for the desired cell.
- **Player 2**: Connects to the server and plays as 'O'. Player 2 also enters the row and column for their move.

### Communication
- The server communicates with the players over a TCP/IP connection.
- Players input their moves in the format: `row,column` (e.g., `1,1` for the top-left corner).
  

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This game was created as a simple network programming exercise.
- Special thanks to the Python documentation and tutorials for network programming.


