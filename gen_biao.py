import itertools
import json

PATTERNS = "11111", "011110", "011100", "001110", \
           "011010", "010110", "11110", "01111", \
          "11011", "10111", "11101", "001100", \
          "001010", "010100", "000100", "001000"

PATTERN_SCORES = 50000, 4320, 720, 720, 720, 720, 720, 720, 720, 720, 720, 120, 120, 120, 20, 20

a = [0, 1, 2]
aa = []
for i in range(5, 10):
    print(i)
    aa += list(itertools.permutations(a, i))

js = json.dumps(aa)
with open("../config/record.json","w") as f:
    json.dump(js,f)


