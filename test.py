import numpy as np
import wdnmd

chessboard = np.zeros((15, 15), dtype=np.int)
chessboard[7, 7] = 1


print(chessboard)
aaa = wdnmd.AI(15, -1, 5)
aaa.go(chessboard)
print(aaa.candidate_list)

