import socket
from rpc_runtime import send_msg, recv_msg

def rpc_call(method, params):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 5000))

    send_msg(sock, {
        "method": method,
        "params": params
    })

    response = recv_msg(sock)
    sock.close()
    return response["result"]

if __name__ == "__main__":
    print("Add:", rpc_call("add", [3, 4]))
    print("Multiply:", rpc_call("multiply", [3, 4]))
