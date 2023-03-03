WIDTH = 19
HEIGHT = 19

FLIP_NONE = 0
FLIP_H = 1
FLIP_V = 2
FLIP_V_AND_H = 3

grid = list()


def init_grid():
    grid = list()
    f = open("grid.txt", "r")

    line = f.readline()
    while line != "":
        grid.append([*line.strip()])
        line = f.readline()
    f.close()
    return grid


red_curve = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 5],
    [3, 5],
    [4, 5],
    [4, 6],
    [5, 6],
    [6, 6],
    [7, 6],
    [7, 7],
    [7, 8],
    [8, 8],
    [8, 9],
    [8, 10],
    [8, 11],
    [9, 11],
    [10, 11],
    [10, 12],
    [10, 13],
    [10, 14],
    [11, 14],
    [12, 14],
    [12, 15],
    [12, 16],
]

yellow_curve = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [1, 5],
    [2, 5],
    [3, 5],
    [3, 6],
    [3, 7],
    [4, 7],
    [4, 8],
    [4, 9],
    [5, 9],
    [6, 9],
    [7, 9],
    [8, 9],
    [8, 10],
    [8, 11],
    [8, 12],
    [9, 12],
    [10, 12],
    [11, 12],
    [11, 13],
    [11, 14],
    [11, 15],
    [11, 16],
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

curves = {
    "red": red_curve,
    "yellow": yellow_curve,
    "brown": brown_curve,
    "striped": striped_curve,
}


def draw_grid():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            print(grid[i][j], end="")
        print()


def fits(curve, x_start, y_start):
    # print(x_start)
    # print(y_start)
    # print(curve)
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        # print(f"{x}-{y}")
        if x >= WIDTH or y >= HEIGHT:
            return False
        if grid[x][y] != ".":
            return False
    return True


def put(curve, x_start, y_start, sign):
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = sign


def delete(curve, x_start, y_start):
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = "."


def flip_v(curve):
    result = list()
    width = curve[len(curve) - 1][0]
    for point in reversed(curve):
        result.append([width - point[0], point[1]])
    return result


def flip_h(curve):
    result = list()
    height = curve[len(curve) - 1][1]
    for point in reversed(curve):
        result.append([point[0], height - point[1]])
        # print([point[0], height - point[1]])
    return result


def flip_v_and_h(curve):
    result = list()
    width = curve[len(curve) - 1][0]
    height = curve[len(curve) - 1][1]
    for point in curve:
        result.append([width - point[0], height - point[1]])
    return result


def flip(curve, flip_type):
    if flip_type == FLIP_V:
        return flip_v(curve)
    if flip_type == FLIP_H:
        return flip_h(curve)
    if flip_type == FLIP_V_AND_H:
        return flip_v_and_h(curve)
    # no flip
    return curve


def get_width(curve):
    begin = curve[0][0]
    end = curve[len(curve) - 1][0]
    return max(begin, end)


def get_height(curve):
    begin = curve[0][1]
    end = curve[len(curve) - 1][1]
    return max(begin, end)


def get_possible_starts(curve):
    possible_starts = list()

    curve_width = get_width(curve)  # curve[len(curve) - 1][0]
    curve_height = get_height(curve)  # curve[len(curve) - 1][1]

    for i in range(WIDTH - curve_width):
        for j in range(HEIGHT - curve_height):
            if fits(curve, i, j):
                possible_starts.append([i, j])

    # print("possible starts: ")
    # print(possible_starts)
    return possible_starts


def try_combination(curve_1, curve_2, curve_3, curve_4, c1, c2, c3, c4):
    first_curve_starts = get_possible_starts(curve_1)
    for start_1 in first_curve_starts:
        put(curve_1, start_1[0], start_1[1], c1)
        second_curve_starts = get_possible_starts(curve_2)
        for start_2 in second_curve_starts:
            put(curve_2, start_2[0], start_2[1], c2)
            third_curve_starts = get_possible_starts(curve_3)
            for start_3 in third_curve_starts:
                put(curve_3, start_3[0], start_3[1], c3)
                fourth_curve_starts = get_possible_starts(curve_4)
                if len(fourth_curve_starts) > 0:
                    for start_4 in fourth_curve_starts:
                        put(curve_4, start_4[0], start_4[1], c4)
                        print("SUCCESS !!!")
                        draw_grid()
                delete(curve_3, start_3[0], start_3[1])
            delete(curve_2, start_2[0], start_2[1])
        delete(curve_1, start_1[0], start_1[1])


def brute_force():
    nb_tries = 0

    for a in range(len(curves)):
        key_a = list(curves.keys())[a]
        for flip_a in range(4):
            curve_a = flip(curves.get(key_a), flip_a)
            for b in range(len(curves)):
                if b != a:
                    key_b = list(curves.keys())[b]
                    for flip_b in range(4):
                        curve_b = flip(curves.get(key_b), flip_b)
                        for c in range(len(curves)):
                            if c != a and c != b:
                                key_c = list(curves.keys())[c]
                                for flip_c in range(4):
                                    curve_c = flip(curves.get(key_c), flip_c)
                                    for d in range(len(curves)):
                                        if d != a and d != b and d != c:
                                            key_d = list(curves.keys())[d]
                                            for flip_d in range(4):
                                                curve_d = flip(
                                                    curves.get(key_d), flip_d
                                                )
                                                # print(
                                                #     f"{key_a} {key_b} {key_c} {key_d} "
                                                # )
                                                try_combination(
                                                    curve_a,
                                                    curve_b,
                                                    curve_c,
                                                    curve_d,
                                                    key_a[0],
                                                    key_b[0],
                                                    key_c[0],
                                                    key_d[0],
                                                )
                                                nb_tries += 1

    print(nb_tries)


grid = init_grid()
brute_force()


def test():
    grid = init_grid()
    put(flip_v_and_h(striped_curve), 0, 6, "s")
    put(yellow_curve, 1, 0, "y")
    put(red_curve, 5, 2, "r")
    put(brown_curve, 3, 0, "b")
    draw_grid()
