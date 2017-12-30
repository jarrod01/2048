import random

score = 0
level = 0

# level 决定每次随机出现的数字的概率以及最大的数字是多少
# level 0: 随机出现2和4，概率各位50%
# level 1：随机出现2、4、8，概率分别为45% 45% 10%
# level 2：随机出现2、4、8、16，概率分别为40% 40% 10% 10%
# level 3: 随机出现2、4、8、16、32
def generater_number(level=0):
    tmp = random.randint(0, 9)
    if tmp < 10-level:
        chosen_number = random.sample([2,4], 1)[0]
    else:
        chosen_number = 2**(tmp-(10-level)+3)
    return chosen_number

def next_index(numbers):
    indexes = []
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == 0:
                indexes.append((i, j))
    if not indexes:
        return numbers
    else:
        index = random.sample(indexes, 1)[0]
        numbers[index[0]][index[1]] = generater_number(level)
    # 根据初始数字和级别随机生成2个数字
    return numbers

# start_number 决定初始数字是多少，
def game_initializer(start_number=0, level=0):
    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    indexes = []
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == 0:
                indexes.append((i, j))
    first_indexes = random.sample(indexes, 2)
    # 根据初始数字和级别随机生成2个数字
    if start_number:
        first_numbers = [start_number]
    else:
        first_numbers = [generater_number(level)]
    first_numbers.append(generater_number(level))
    for i in range(2):
        numbers[first_indexes[i][0]][first_indexes[i][1]] = first_numbers[i]
    return numbers

def move(numbers, direction):
    score = 0
    moved = False
    if direction == 'right' or direction == 'r':
        for i in range(4):
            line = numbers[i].copy()
            # 将0去掉
            for j in range(line.count(0)):
                line.remove(0)
            # 将可以相加的相加
            j = len(line)-1
            while j > 0:
                if line[j] == line[j-1]:
                    line[j] *= 2
                    score += line[j]
                    line.pop(j - 1)
                    j -= 2
                else:
                    j -= 1
            # 补齐
            line = [0] * (4-len(line)) + line
            if line != numbers[i]:
                moved = True
                numbers[i] = line.copy()

    elif direction == 'left' or direction == 'l':
        for i in range(4):
            line = numbers[i].copy()
            # 将0去掉
            for j in range(line.count(0)):
                line.remove(0)
            # 将可以相加的相加
            j = 0
            while j < len(line)-1:
                if line[j] == line[j+1]:
                    line[j] *= 2
                    score += line[j]
                    line.pop(j + 1)
                    j += 1
                else:
                    j += 1
            # 补齐
            line = line + [0] * (4-len(line))
            if line != numbers[i]:
                moved = True
                numbers[i] = line.copy()

    elif direction == 'down' or direction == 'd':
        for i in range(4):
            original_col = []
            for j in range(4):
                original_col.append(numbers[j][i])
            line = original_col.copy()
            # 将0去掉
            for j in range(line.count(0)):
                line.remove(0)
            # 将可以相加的相加
            j = len(line)-1
            while j > 0:
                if line[j] == line[j-1]:
                    line[j] *= 2
                    score += line[j]
                    line.pop(j - 1)
                    j -= 2
                else:
                    j -= 1
            # 补齐
            line = [0] * (4-len(line)) + line
            if line != original_col:
                moved = True
                for j in range(4):
                    numbers[j][i] = line[j]

    elif direction == 'up' or direction == 'u':
        for i in range(4):
            original_col = []
            for j in range(4):
                original_col.append(numbers[j][i])
            line = original_col.copy()
            # 将0去掉
            for j in range(line.count(0)):
                line.remove(0)
            # 将可以相加的相加
            j = 0
            while j < len(line)-1:
                if line[j] == line[j+1]:
                    line[j] *= 2
                    score += line[j]
                    line.pop(j + 1)
                    j += 1
                else:
                    j += 1
            # 补齐
            line = line + [0] * (4-len(line))
            if line != original_col:
                moved = True
                for j in range(4):
                    numbers[j][i] = line[j]

    return {'nums': numbers, 'moved': moved, 'score': score}

def print_number(numbers):
    for i in range(4):
        tmp = ''
        for j in range(4):
            tmp += (str(numbers[i][j]) + '\t')
        print(tmp)
    print('\n')

def died_or_not(numers):
    directions = ['left', 'right', 'up', 'down']
    died = True
    for direction in directions:
        result = move(numbers, direction)
        if result['moved']:
            died = False
            break
    return died

if __name__ == '__main__':
    score = 0
    numbers = game_initializer()
    # print_number(numbers)
    print(numbers)
    died = died_or_not(numbers)
    while not died:
        direction = input('direction:  ')
        result = move(numbers, direction)
        numbers = result['nums']
        score += result['score']
        numbers = next_index(numbers)
        died = died_or_not(numbers)
        # print_number(numbers)
        print(numbers)