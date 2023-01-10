WIDTH = 19
HEIGHT = 19

grid = list()

f = open("grid.txt", "r")

line = f.readline()
while line != "":
    grid.append([*line.strip()])
    line = f.readline()
f.close()

red_curve = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [3, 1],
    [4, 1],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
    [6, 4],
    [6, 5],
    [6, 6],
    [6, 7],
    [7, 7],
    [8, 7],
    [8, 8],
    [9, 8],
    [10, 8],
    [11, 8],
    [11, 9],
    [11, 10],
    [12, 10],
    [13, 10],
    [14, 10],
    [14, 11],
    [14, 12],
    [15, 12],
    [16, 12],
]

yellow_curve = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [5, 1],
    [5, 2],
    [5, 3],
    [6, 3],
    [7, 3],
    [7, 4],
    [8, 4],
    [9, 4],
    [9, 5],
    [9, 6],
    [9, 7],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [12, 9],
    [12, 10],
    [12, 11],
    [13, 11],
    [14, 11],
    [15, 11],
    [16, 11],
]

brown_curve = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [3, 1],
    [3, 2],
    [4, 2],
    [5, 2],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [7, 5],
    [7, 6],
    [7, 7],
    [8, 7],
    [9, 7],
    [10, 7],
    [11, 7],
    [11, 8],
    [11, 9],
    [12, 9],
    [12, 10],
    [12, 11],
    [12, 12],
    [13, 12],
    [14, 12],
    [15, 12],
]

striped_curve = [
    [0, 0],
    [1, 0],
    [2, 0],
    [2, 1],
    [3, 1],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
    [5, 4],
    [5, 5],
    [6, 5],
    [7, 5],
    [7, 6],
    [8, 6],
    [9, 6],
    [9, 7],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [12, 9],
    [12, 10],
    [12, 11],
    [12, 12],
    [13, 12],
    [14, 12],
    [15, 12],
]


def draw_grid():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            print(grid[i][j], end="")
        print()


def fits(curve, x_start, y_start):
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        if grid[x][y] != ".":
            return False
    return True


def put(curve, x_start, y_start, sign):
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = sign


def flip_h(curve):
    result = list()
    width = curve[len(curve) - 1][0]
    for point in curve:
        result.append([width - point[0], point[1]])
    return result


def flip_v(curve):
    result = list()
    height = curve[len(curve) - 1][1]
    for point in curve:
        result.append([point[0], height - point[1]])
    return result


def flip_v_and_h(curve):
    result = list()
    width = curve[len(curve) - 1][0]
    height = curve[len(curve) - 1][1]
    for point in curve:
        result.append([width - point[0], height - point[1]])
    return result


def try_reds():
    possible_reds = list()

    red_width = red_curve[len(red_curve) - 1][0]
    red_height = red_curve[len(red_curve) - 1][1]

    for i in range(WIDTH - red_width):
        for j in range(HEIGHT - red_height):
            if fits(red_curve, i, j):
                possible_reds.append([i, j])

    print("possible red starts: ")
    print(possible_reds)


def try_yellows():
    possible_yellows = list()

    yellow_width = yellow_curve[len(yellow_curve) - 1][0]
    yellow_height = yellow_curve[len(yellow_curve) - 1][1]

    for i in range(WIDTH - yellow_width):
        for j in range(HEIGHT - yellow_height):
            if fits(yellow_curve, i, j):
                possible_yellows.append([i, j])

    print("possible yellow starts: ")
    print(possible_yellows)


def try_browns():
    possible_browns = list()

    brown_width = brown_curve[len(brown_curve) - 1][0]
    brown_height = brown_curve[len(brown_curve) - 1][1]

    for i in range(WIDTH - brown_width):
        for j in range(HEIGHT - brown_height):
            if fits(brown_curve, i, j):
                possible_browns.append([i, j])

    print("possible brown starts: ")
    print(possible_browns)


def try_striped():
    possible_striped = list()

    striped_width = striped_curve[len(striped_curve) - 1][0]
    striped_height = striped_curve[len(striped_curve) - 1][1]

    for i in range(WIDTH - striped_width):
        for j in range(HEIGHT - striped_height):
            if fits(striped_curve, i, j):
                possible_striped.append([i, j])

    print("possible striped starts: ")
    print(possible_striped)


put(red_curve, 0, 6, "1")

put(flip_v(red_curve), 2, 0, "2")

# put(yellow_curve, 2, 0, "y")
# put(brown_curve, 1, 3, "b")

draw_grid()

# cases :
# base
# flip_h
# flip_v
# flip_h + flip_v
