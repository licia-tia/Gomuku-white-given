import numpy as np
import wdnmd
import time

chessboard = np.zeros((15, 15), dtype=np.int)
chessboard[2, 2] = 1
chessboard[3, 3] = 1
chessboard[4, 4] = 1
chessboard[5, 6] = 1
chessboard[5, 8] = 1
chessboard[1:3, 11] = -1
chessboard[3, 9:11] = -1
chessboard[6, 13] = -1

print(chessboard)

print()
a = wdnmd.AI(15, -1, 5)
start = time.time()
# a.eval_pos(chessboard, 1, 9)
# a.eval_pos(chessboard, 7, 9)
a.go(chessboard)
print(a.candidate_list)
# for p in range(1000):
#     a.go(chessboard)


print(time.time()-start)
