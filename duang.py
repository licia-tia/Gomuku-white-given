import itertools
import json

ATK = 30
PATTERNS = "11111", "011110", "011100", "001110", \
           "011010", "010110", "11110", "01111", \
           "11011", "10111", "11101", "001100", \
           "001010", "010100", "000100", "001000"

PATTERN_SCORES = 50000, 4320, 720, 720, 720, 720, 720, 720, 720, 720, 720, 120, 120, 120, 20, 20


def getscore(p):
    tmp = ''
    for i in p:
        if i == 2:
            tmp+='1'
        elif i == 1:
            tmp+='1'
        elif i==0:
            tmp+='0'
        else:
            tmp+='2'

    result = 0
    # print(tmp)
    for j in range(len(PATTERNS)):
        if PATTERNS[j] in tmp:
            result += PATTERN_SCORES[j]
            break

    tmp = ''
    for i in p:
        if i == 2:
            tmp+='1'
        elif i == 1:
            tmp+='2'
        elif i==0:
            tmp+='0'
        else:
            tmp+='1'
    # print(tmp)

    for j in range(len(PATTERNS)):
        if PATTERNS[j] in tmp:
            result += PATTERN_SCORES[j]
            break

    return result


def getscore_1(p):
    tmp = ''
    for i in p:
        if i == 2:
            tmp+='1'
        elif i == 1:
            tmp+='2'
        elif i==0:
            tmp+='0'
        else:
            tmp+='1'

    result = 0
    # print(tmp)
    for j in range(len(PATTERNS)):
        if PATTERNS[j] in tmp:
            result += PATTERN_SCORES[j]
            break

    tmp = ''
    for i in p:
        if i == 2:
            tmp+='1'
        elif i == 1:
            tmp+='1'
        elif i==0:
            tmp+='0'
        else:
            tmp+='2'
    # print(tmp)

    for j in range(len(PATTERNS)):
        if PATTERNS[j] in tmp:
            result += PATTERN_SCORES[j]
            break

    return result


# print(getscore([0, 0, 0, 2, -1, -1, 0, 0, 0]))

a = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        for kk in range(-1, 2):
                            for ll in range(-1, 2):
                                for iii in range(-1, 2):
                                    # tmp = ''
                                    # tmp = tmp +'['+ str(i) +' '+ str(j) +' '+ str(k) +' '+ str(l) +' '+ str(ii)+' '+str(jj)+' '+str(kk)+' '+str(ll)+' '+str(iii)+ ']'
                                    tmp = [i, j, k, l, ii, jj, kk ,ll, iii]
                                    a.append(tmp)

for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        for kk in range(-1, 2):
                            for ll in range(-1, 2):

                                # tmp = ''
                                # tmp = tmp + '['+str(i) + ' '+str(j) + ' '+str(k) + ' '+str(l) + ' '+str(ii)+' '+str(jj)+' '+str(kk)+' '+str(ll)+ ']'
                                tmp = [i, j, k, l, ii, jj, kk ,ll]
                                a.append(tmp)


for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        for kk in range(-1, 2):
                            # tmp = ''
                            # tmp = tmp + '['+str(i) + ' '+str(j) + ' '+str(k) + ' '+str(l) + ' '+str(ii)+' '+str(jj)+' '+str(kk)+ ']'
                            tmp = [i, j, k, l, ii, jj, kk]
                            a.append(tmp)


for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        # tmp = ''
                        # tmp = tmp + '['+str(i) +' '+ str(j) +' '+ str(k) +' '+ str(l) + ' '+str(ii)+' '+str(jj)+ ']'
                        tmp = [i, j, k, l, ii, jj]
                        a.append(tmp)

# for i in range(-1, 2):
#     for j in range(-1, 2):
#         for k in range(-1, 2):
#             for l in range(-1, 2):
#                 for ii in range(-1, 2):
#                     tmp = ''
#                     tmp = tmp + str(i) + ' '+str(j) + ' '+str(k) + ' '+str(l) +' '+ str(ii)
#                     a.append(tmp)

a.append([1, 1, 1, 1, 1])
a.append([-1, -1, -1, -1, -1])
c = []
for i in a:
    for j in range(len(i)):
        tmp = i.copy()
        tmp[j] = 2
        c.append(tmp)
        # if tmp == [1, 0, 1, 2, 0, 0]:
        #     print('!')
b = {}

for i in c:
    tmp = getscore(i)
    if tmp != 0 :
        b.setdefault(tuple(i), tmp)

d = {}

for i in c:
    tmp = getscore_1(i)
    if tmp != 0 :
        d.setdefault(tuple(i), tmp)


with open("record_neg.json","w") as f:
    f.write(str(b))

with open("record_pos.json","w") as f:
    f.write(str(d))
