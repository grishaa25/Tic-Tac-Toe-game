import socket

def print_board(board):
    for i in range(3):
        print(board[i*3] + '|' + board[i*3+1] + '|' + board[i*3+2])
        if i < 2:
            print('-----')

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        try:
            message = client.recv(1024).decode()

            if len(message) == 9:  
                print_board(message)
            else:
                print(message)

            if 'Your turn' in message:
                move = input('Enter position (0-8): ')
                client.send(move.encode())
        except ConnectionAbortedError:
            print("Game over.")
            break


if __name__ == '__main__':
    start_client()
    
