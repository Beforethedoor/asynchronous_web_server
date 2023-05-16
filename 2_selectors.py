import selectors
import socket

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()

    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,
        data=accept_connection
    )


def accept_connection(server_socket):
    client_socket, addres = server_socket.accept()
    print(f"Connection from: {addres}")
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello world!".encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events: tuple = selector.select()  # (key, events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
