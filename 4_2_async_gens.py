import socket
from collections import deque
from select import select

tasks = deque()
to_read = dict()
to_write = dict()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("localhost", 8000))
    server_socket.listen()

    while True:
        yield ("read", server_socket)
        client_socket, addres = server_socket.accept()
        print(f"Connection from: {addres}")
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ("read", client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello world".encode()
            yield ("write", client_socket)
            client_socket.send(response)

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_wtite, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            for sock in ready_to_wtite:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.popleft()
            reason, sock = next(task)

            if reason == "read":
                to_read[sock] = task
            if reason == "write":
                to_write[sock] = task
        except StopIteration:
            pass


if __name__ == "__main__":
    tasks.append(server())
    event_loop()
