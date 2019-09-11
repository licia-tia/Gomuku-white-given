import numpy as np
import wdnmd

chessboard = np.zeros((15, 15), dtype=np.int)

# chessboard = np.ones((15, 15))
# chessboard[:, ::2] = -1
# for i in range(0, 15, 4):
#     chessboard[i] = -chessboard[i]
# x, y = np.random.choice(15, 2)
# chessboard[x, y] = 0

chessboard[2, 2] = 1
chessboard[2, 4] = 1
chessboard[3, 2:4] = 1
chessboard[5, 2] = 1
chessboard[1, 10:12] = -1
chessboard[2, 10] = -1
chessboard[4, 12:14] = -1


print(chessboard)
aaa = wdnmd.AI(15, -1, 5)
aaa.go(chessboard)



