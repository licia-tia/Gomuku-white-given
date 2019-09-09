import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

# 模式
paterns = "11111", "011110", "011100", "001110", \
          "011010", "010110", "11110", "01111", \
          "11011", "10111", "11101", "001100", \
          "001010", "010100", "000100", "001000"

# 模式相应的分数
patern_scores = 50000, 4320, 720, 720, 720, 720, 720, 720, 720, 720, 720, 120, 120, 120, 20, 20


class AI(object):

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # My color
        self.color = color
        # max time
        self.time_out = time_out
        # add decision into candidate_list
        self.candidate_list = []

    def eval_pos(self, chessboard, x, y):
        lines_mine = ['', '', '', '']
        lines_bad = ['', '', '', '']
        for i in range(max(0, x - 4), min(self.chessboard_size - 1, x + 4)):
            if i == x:
                lines_mine[0] += '1'
                lines_bad[0] += '1'
            else:
                if chessboard[i][y] == self.color:
                    lines_mine[0] += '1'
                    lines_bad[0] += '2'
                elif chessboard[i][y] == COLOR_NONE:
                    lines_mine[0] += '0'
                    lines_bad[0] += '0'
                else:
                    lines_mine[0] += '2'
                    lines_bad[0] += '1'

        for i in range(max(0, y - 4), min(self.chessboard_size - 1, y + 4)):
            if i == y:
                lines_mine[1] += '1'
                lines_bad[1] += '1'
            else:
                if chessboard[x][i] == self.color:
                    lines_mine[1] += '1'
                    lines_bad[1] += '2'
                elif chessboard[x][i] == COLOR_NONE:
                    lines_mine[1] += '0'
                    lines_bad[1] += '0'
                else:
                    lines_mine[1] += '2'
                    lines_bad[1] += '1'

        i = x - min(x, y, 4)
        j = y - min(x, y, 4)

        while i < min(self.chessboard_size, x + 5) and j < min(self.chessboard_size, y + 5):
            if i == x and j == y:
                lines_mine[2] += '1'
                lines_bad[2] += '1'
            else:
                if chessboard[i][j] == self.color:
                    lines_mine[2] += '1'
                    lines_bad[2] += '2'
                elif chessboard[i][j] == COLOR_NONE:
                    lines_mine[2] += '0'
                    lines_bad[2] += '0'
                else:
                    lines_mine[2] += '2'
                    lines_bad[2] += '1'
            i = i + 1
            j = j + 1

        i = x + min(y, self.chessboard_size - 1 - x, 4)
        j = y - min(y, self.chessboard_size - 1 - x, 4)

        while i >= max(0, x - 5) and j < min(self.chessboard_size, y + 5):
            if i == x and j == y:
                lines_mine[3] += '1'
                lines_bad[3] += '1'
            else:
                if chessboard[i][j] == self.color:
                    lines_mine[3] += '1'
                    lines_bad[3] += '2'
                elif chessboard[i][j] == COLOR_NONE:
                    lines_mine[3] += '0'
                    lines_bad[3] += '0'
                else:
                    lines_mine[3] += '2'
                    lines_bad[3] += '1'
            i = i - 1
            j = j + 1

        result = 0

        for i in lines_mine:
            for j in range(len(paterns)):
                if paterns[j] in i:
                    result = result + patern_scores[j] + 30
                    break

        for i in lines_bad:
            for j in range(len(paterns)):
                if paterns[j] in i:
                    result = result + patern_scores[j] - 30
                    break

        return result

        # The input is current chessboard

    def go(self, chessboard):
        # clear candidate_list
        self.candidate_list.clear()

        # My white giving show

        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        # pos_idx = random.randint(0, len(idx) - 1)
        # new_pos = idx[pos_idx]

        max_score = 0
        new_pos = [0, 0]

        # for i in range(self.chessboard_size):
        #     for j in range(self.chessboard_size):

        for i, j in idx:
            score = self.eval_pos(chessboard, i, j)
            if score >= max_score:
                max_score = score
                new_pos[0] = i
                new_pos[1] = j

        # done
        if len(idx) == self.chessboard_size * self.chessboard_size:
            new_pos[0] = int(self.chessboard_size / 2)
            new_pos[1] = int(self.chessboard_size / 2)

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE
        self.candidate_list.append(new_pos)
