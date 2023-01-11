WIDTH = 19
HEIGHT = 19

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


def delete(curve, x_start, y_start):
    for point in curve:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = "."


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


def get_possible_starts(curve):
    possible_starts = list()

    curve_width = curve[len(curve) - 1][0]
    curve_height = curve[len(curve) - 1][1]

    for i in range(WIDTH - curve_width):
        for j in range(HEIGHT - curve_height):
            if fits(curve, i, j):
                possible_starts.append([i, j])

    # print("possible starts: ")
    # print(possible_starts)
    return possible_starts


def try_combination(curve_1, curve_2, curve_3, curve_4):
    first_curve_starts = get_possible_starts(curve_1)
    for start_1 in first_curve_starts:
        # print(f"lvl1 : {start_1}")
        put(curve_1, start_1[0], start_1[1], "1")
        second_curve_starts = get_possible_starts(curve_2)
        for start_2 in second_curve_starts:
            # print(f"lvl2 : {start_2}")
            put(curve_2, start_2[0], start_2[1], "2")
            third_curve_starts = get_possible_starts(curve_3)
            for start_3 in third_curve_starts:
                # print(f"lvl3 : {start_3}")
                put(curve_3, start_3[0], start_3[1], "3")
                fourth_curve_starts = get_possible_starts(curve_4)
                if len(fourth_curve_starts) > 0:
                    print("SUCCESS !!!")
                # else:
                # print("nope...")
                delete(curve_3, start_3[0], start_3[1])
            delete(curve_2, start_2[0], start_2[1])
        delete(curve_1, start_1[0], start_1[1])


grid = init_grid()

# put(yellow_curve, 2, 0, "y")
# put(brown_curve, 1, 3, "b")

for a in range(len(curves)):
    key_a = list(curves.keys())[a]
    for b in range(len(curves)):
        if b != a:
            key_b = list(curves.keys())[b]
            for c in range(len(curves)):
                if c != a and c != b:
                    key_c = list(curves.keys())[c]
                    for d in range(len(curves)):
                        if d != a and d != b and d != c:
                            key_d = list(curves.keys())[d]
                            # print(f"{key_a} {key_b} {key_c} {key_d} ")
                            try_combination(
                                curves.get(key_a),
                                curves.get(key_b),
                                curves.get(key_c),
                                curves.get(key_d),
                            )


# draw_grid()


# cases :
# base
# flip_h
# flip_v
# flip_h + flip_v

# 4 base
# 4 flip_h
# 4 flip_v
# 4 flip_v_and_h

# 3 base + 1 flip_h
# 3 base + 1 flip_v
# 3 base + 1 flip_v_and_h

# 2 base + 2 flip_h
# 2 base + 2 flip_v
# 2 base + 2 flip_v_and_h

# 2 base + 1 flip_v


# from itertools import permutations, combinations

# elements = ['a', 'b', 'c', 'd']
# states = ['e1', 'e2', 'e3', 'e4']

# # Génération de toutes les combinaisons d'éléments
# combinations = list(combinations(elements, 4))

# # Génération de toutes les combinaisons d'états
# state_combinations = list(combinations(states, 4))

# # Génération de toutes les permutations d'éléments
# permutations = list(permutations(elements))

# # Génération de toutes les permutations d'états
# state_permutations = list(permutations(states))

# # Génération de toutes les combinaisons d'éléments et d'états
# combination_and_permutations = []
# for c in combinations:
#     for s in state_combinations:
#         combination_and_permutations.append(list(zip(c,s)))
