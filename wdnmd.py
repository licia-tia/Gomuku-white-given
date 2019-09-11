import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
debug = []
ATK = 30
DEPTH = 3

# 模式
PATTERNS = "11111", "011110", "011100", "001110", \
           "011010", "010110", "11110", "01111", \
           "11011", "10111", "11101", "001100", \
           "001010", "010100", "000100", "001000"

# 模式相应的分数
PATTERN_SCORES = 50000, 4320, 720, 720, 720, 720, 720, 720, 720, 720, 720, 120, 120, 120, 20, 20


class AI(object):

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # My color
        self.color = color
        # max time
        self.time_out = time_out
        # add decision into candidate_list
        self.candidate_list = []
        self.empty_idx = np.where(np.zeros((chessboard_size, chessboard_size), dtype=np.int) == COLOR_NONE)
        self.empty_idx = list(zip(self.empty_idx[0], self.empty_idx[1]))

    def eval_pos(self, chessboard, x, y, role):
        lines_mine = ['', '', '', '']
        lines_bad = ['', '', '', '']
        for i in range(max(0, x - 4), min(self.chessboard_size, x + 5)):
            if i == x:
                lines_mine[0] += '1'
                lines_bad[0] += '1'
            else:
                if chessboard[i][y] == role:
                    lines_mine[0] += '1'
                    lines_bad[0] += '2'
                elif chessboard[i][y] == COLOR_NONE:
                    lines_mine[0] += '0'
                    lines_bad[0] += '0'
                else:
                    lines_mine[0] += '2'
                    lines_bad[0] += '1'

        for i in range(max(0, y - 4), min(self.chessboard_size, y + 5)):
            if i == y:
                lines_mine[1] += '1'
                lines_bad[1] += '1'
            else:
                if chessboard[x][i] == role:
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
                if chessboard[i][j] == role:
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
                if chessboard[i][j] == role:
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
            for j in range(len(PATTERNS)):
                if PATTERNS[j] in i:
                    result = result + PATTERN_SCORES[j] + ATK
                    break

        for i in lines_bad:
            for j in range(len(PATTERNS)):
                if PATTERNS[j] in i:
                    result = result + PATTERN_SCORES[j] - ATK
                    break

        return result

        # The input is current chessboard

    def eval_map(self, chessboard, role):
        lines_mine = []
        lines_bad = []
        count = 0

        for i in range(0, self.chessboard_size):
            lines_mine.append('')
            lines_bad.append('')
            for j in range(0, self.chessboard_size):
                if chessboard[i][j] == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif chessboard[i][j] == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        for i in range(0, self.chessboard_size):
            lines_mine.append('')
            lines_bad.append('')
            for j in range(0, self.chessboard_size):
                if chessboard[j][i] == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif chessboard[j][i] == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        for i in range(self.chessboard_size):
            res = [chessboard[i + k, 0 + k] for k in range(self.chessboard_size - i)]
            lines_mine.append('')
            lines_bad.append('')
            for j in res:
                if j == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif j == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        for i in range(self.chessboard_size):
            res = [chessboard[0 + k, i + k] for k in range(self.chessboard_size - i - 1)]
            lines_mine.append('')
            lines_bad.append('')
            for j in res:
                if j == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif j == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        for i in range(self.chessboard_size):
            res = [chessboard[i - k, 0 + k] for k in range(self.chessboard_size - i)]
            lines_mine.append('')
            lines_bad.append('')
            for j in res:
                if j == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif j == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        for i in range(self.chessboard_size):
            res = [chessboard[0 + k, i - k] for k in range(self.chessboard_size - i - 1)]
            lines_mine.append('')
            lines_bad.append('')
            for j in res:
                if j == role:
                    lines_mine[count] += '1'
                    lines_bad[count] += '2'
                elif j == COLOR_NONE:
                    lines_mine[count] += '0'
                    lines_bad[count] += '0'
                else:
                    lines_mine[count] += '2'
                    lines_bad[count] += '1'
            count = count + 1

        result = 0

        for i in lines_mine:
            for j in range(len(PATTERNS)):
                if PATTERNS[j] in i:
                    result = result + PATTERN_SCORES[j]

        for i in lines_bad:
            for j in range(len(PATTERNS)):
                if PATTERNS[j] in i:
                    result = result - PATTERN_SCORES[j]

        return result

    def minimax(self, chessboard, depth, idx):
        if depth % 2 == 0:
            role = -self.color
        else:
            role = self.color
        if depth == DEPTH or depth == 0:
            return self.eval_map(chessboard, role)


        elif depth % 2 != 0:
            score = -999999999999999
            for i in range(len(idx)):
                # ===============
                near = []
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            near.append(chessboard[idx[i][0] + j][idx[i][1] + k])
                        except Exception:
                            pass

                if not ((COLOR_WHITE in near) or (COLOR_BLACK in near)):
                    idx[i] = (-1, -1)
                    continue
                # ============
                if idx[i] == (-1, -1):
                    continue
                idx_tmp = idx.copy()
                idx_tmp[i] = (-1, -1)
                chessboard_tmp = np.copy(chessboard)
                chessboard_tmp[idx[i][0]][idx[i][1]] = self.color
                score = max(score, self.minimax(chessboard_tmp, depth + 1, idx_tmp))
            return score
        else:
            score = 999999999999999
            for i in range(len(idx)):

                near = []
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            near.append(chessboard[idx[i][0] + j][idx[i][1] + k])
                        except Exception:
                            pass

                if not ((COLOR_WHITE in near) or (COLOR_BLACK in near)):
                    idx[i] = (-1, -1)
                    continue
                # ============

                if idx[i] == (-1, -1):
                    continue
                idx_tmp = idx.copy()
                idx_tmp[i] = (-1, -1)
                chessboard_tmp = np.copy(chessboard)
                chessboard_tmp[idx[i][0]][idx[i][1]] = self.color
                score = min(score, self.minimax(chessboard_tmp, depth + 1, idx_tmp))
            return score

    def more_than_single(self, chessboard, idx):
        max_score = -1
        new_pos = [0, 0]
        # 如果空盘，下中间
        if len(idx) == self.chessboard_size * self.chessboard_size:
            new_pos[0] = int(self.chessboard_size / 2)
            new_pos[1] = int(self.chessboard_size / 2)
        elif len(idx) == 1:
            new_pos = idx[0]
        else:
            max_score = -9999999999999999999999
            for i in range(len(idx)):
                if idx[i] == (-1, -1):
                    continue

                near = []
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        try:
                            near.append(chessboard[idx[i][0] + j][idx[i][1] + k])
                        except Exception:
                            pass

                if (COLOR_WHITE in near) or (COLOR_BLACK in near):
                    idx_tmp = idx.copy()
                    idx_tmp[i] = (0, 0)
                    chessboard_tmp = np.copy(chessboard)
                    chessboard_tmp[idx[i][0]][idx[i][1]] = self.color
                    score = self.minimax(chessboard_tmp, 2, idx_tmp)
                    print(score, (idx[i]))
                    if score > max_score:
                        max_score = score
                        new_pos = idx[i]
                else:
                    idx[i] = (-1, -1)

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE
        self.candidate_list.append(new_pos)

    def single(self, chessboard, idx):
        max_score = -1
        new_pos = [0, 0]
        # 获取新下的棋子
        try:
            new_chess = set(self.empty_idx).difference(set(idx))
            if len(new_chess) != 0:
                tmp = new_chess.pop()
                a = tmp[0]
                b = tmp[1]
                pre_pos = []
                for i in range(a - 1, a + 2):
                    for j in range(b - 1, b + 2):
                        try:
                            if chessboard[i][j] == COLOR_NONE:
                                pre_pos.append((i, j))

                        except Exception:
                            pass

                for i, j in pre_pos:
                    score = self.eval_pos(chessboard, i, j, self.color)
                    if score > max_score:
                        max_score = score
                        new_pos[0] = i
                        new_pos[1] = j

        except Exception:
            pass

        for i, j in idx:
            score = self.eval_pos(chessboard, i, j, self.color)
            if score > max_score:
                max_score = score
                new_pos[0] = i
                new_pos[1] = j

        # 如果空盘，下中间
        if len(idx) == self.chessboard_size * self.chessboard_size:
            new_pos[0] = int(self.chessboard_size / 2)
            new_pos[1] = int(self.chessboard_size / 2)

        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE

        idx.remove((new_pos[0], new_pos[1]))
        self.candidate_list.append(new_pos)

    def go(self, chessboard):
        # clear candidate_list
        self.candidate_list.clear()
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))

        # self.single(chessboard, idx)
        self.more_than_single(chessboard, idx)
        print(self.candidate_list)
