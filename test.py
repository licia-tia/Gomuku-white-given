import numpy as np
import wdnmd

chessboard = np.zeros((15, 15), dtype=np.int)
chessboard[2, 2:4] = 1
chessboard[4, 1:3] = 1
chessboard[1, 10:12] = -1
chessboard[2, 10] = -1
chessboard[4, 12] = -1

print(chessboard)
aaa = wdnmd.AI(15, -1, 5)
aaa.go(chessboard)
print(aaa.eval_pos(chessboard, 1, 9))
print(aaa.eval_pos(chessboard, 3, 2))
