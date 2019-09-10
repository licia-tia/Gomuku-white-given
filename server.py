import socket
import numpy as np

HOST = '0.0.0.0'
PORT = 23333


def beautify_print(self, chessboard):
    char_map = {-1: 'x', 0: ' ', 1: 'o'}

    # print([i for i in range(self.chessboard_size)])

    for i in range(-1, self.chessboard_size):
        print("%4d" % i, end='')
    print()

    for idx, line in enumerate(chessboard):
        # print(line)
        print("%4d" % idx, end='')
        for i in line:
            print("%4s" % char_map[i], end='')
        print()


def interactive_debug(self):
    chessboard = np.zeros((self.chessboard_size, self.chessboard_size), dtype=np.int)
    while True:
        # print(chessboard)
        self.beautify_print(chessboard)

        in_pos_str = input("input next pos: ")
        if in_pos_str == "exit":
            break
        else:
            s1, s2 = in_pos_str.split()[0], in_pos_str.split()[1]
            p1, p2 = int(s1), int(s2)
            chessboard[p1, p2] = 1
            self.__check_result(chessboard, [[7, 7]])
            chessboard[self.agent.candidate_list[-1]] = -1

    pass


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)
while True:
    # 建立客户端连接
    c, addr = s.accept()

    print("连接地址: %s" % str(addr))

    msg = c.recv(1024)
    print(msg.decode())
    i = int(input("x: "))
    j = int(input("y: "))
    msg = '%d,%d' % (i, j)
    c.send(msg.encode('utf-8'))
    c.close()
