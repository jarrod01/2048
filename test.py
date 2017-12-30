line = [0,0,0,2]
original_col = line.copy()
for j in range(4):
    if original_col[j] == 0:
        line.pop(j)