import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


class AI(object):
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # My color
        self.color = color
        # max time
        self.time_out = time_out
        # add decision into candidate_list
        self.candidate_list = []
    # The input is current chessboard
    def go(self, chessboard):
        # clear candidate_list
        self.candidate_list.clear()

        # My white giving show

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        pos_idx = random.randint(0, len(idx)-1)
        new_pos = idx[pos_idx]

        # done

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE
        self.candidate_list.append(new_pos)

