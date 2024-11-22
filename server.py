import socket
import threading

# Initialize the game board
board = [' ' for _ in range(9)]
current_turn = 'X'  
game_over = False
lock = threading.Lock()

def print_board():
    for i in range(3):
        print(board[i*3] + '|' + board[i*3+1] + '|' + board[i*3+2])
        if i < 2:
            print('-----')

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                            (0, 4, 8), (2, 4, 6)]             # Diagonals
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

# Function to check if the game is a draw
def check_draw():
    return ' ' not in board

def handle_client(conn, player_symbol):
    global current_turn, game_over
    conn.send(f'Welcome Player {player_symbol}!'.encode())

    while not game_over:
        with lock:
            if current_turn == player_symbol:
                conn.send('Your turn! Enter a position (0-8): '.encode())
                try:
                    move = int(conn.recv(1024).decode().strip())
                except ValueError:
                    conn.send('Invalid input. Please enter a number between 0 and 8.'.encode())
                    continue

                if move < 0 or move > 8 or board[move] != ' ':
                    conn.send('Invalid move. Try again.'.encode())
                    continue

                board[move] = player_symbol
                current_turn = 'O' if player_symbol == 'X' else 'X'
                update_board()

                # Check for a winner or draw
                winner = check_winner()
                if winner:
                    game_over = True
                    update_board()
                    conn.send(f'Player {winner} wins!'.encode())
                    break
                elif check_draw():
                    game_over = True
                    update_board()
                    conn.send('It\'s a draw!'.encode())
                    break
def update_board():
    board_state = ''.join(board)
    for conn in clients:
        conn.send(board_state.encode())

# Server setup
def start_server():
    global clients
    clients = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)

    print('Tic-Tac-Toe Server Started. Waiting for 2 players...')
    while len(clients) < 2:
        conn, addr = server.accept()
        clients.append(conn)
        print(f'Player {len(clients)} connected from {addr}')

    threading.Thread(target=handle_client, args=(clients[0], 'X')).start()
    threading.Thread(target=handle_client, args=(clients[1], 'O')).start()

if __name__ == '__main__':
    start_server()
    
