WIDTH = 19
HEIGHT = 19

FLIP_NONE = 0
FLIP_H = 1
FLIP_V = 2
FLIP_V_AND_H = 3

nb_positioning_1 = 0
nb_positioning_2 = 0
nb_positioning_3 = 0
nb_positioning_4 = 0

grid = list()

# load the empty grid (available puzzle area)
def init_grid():
    grid = list()
    f = open("grid.txt", "r")

    line = f.readline()
    while line != "":
        grid.append([*line.strip()])
        line = f.readline()
    f.close()
    return grid

# define charts
red_chart = [
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

yellow_chart = [
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

brown_chart = [
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

striped_chart = [
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

charts = {
    "red": red_chart,
    "yellow": yellow_chart,
    "brown": brown_chart,
    "striped": striped_chart,
}

# displays the puzzle area in its current state
def draw_grid():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            print(grid[i][j], end="")
        print()

# checks whether a chart fits in the puzzle area for a given starting point
def fits(chart, x_start, y_start):
    for point in chart:
        x = point[0] + x_start
        y = point[1] + y_start
        if x >= WIDTH or y >= HEIGHT:
            return False
        if grid[x][y] != ".":
            return False
    return True

# updates the puzzle area, positionning a chart on it for a given starting point
def put(chart, x_start, y_start, sign):
    for point in chart:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = sign

# removes a chart from the puzzle area, based on its starting point
def delete(chart, x_start, y_start):
    for point in chart:
        x = point[0] + x_start
        y = point[1] + y_start
        grid[x][y] = "."


# flips a chart vertically
def flip_v(chart):
    result = list()
    width = chart[len(chart) - 1][0]
    for point in reversed(chart):
        result.append([width - point[0], point[1]])
    return result

# flips a chart horizontally
def flip_h(chart):
    result = list()
    height = chart[len(chart) - 1][1]
    for point in reversed(chart):
        result.append([point[0], height - point[1]])
        # print([point[0], height - point[1]])
    return result

# flips a chart vertically and horizontally
def flip_v_and_h(chart):
    result = list()
    width = chart[len(chart) - 1][0]
    height = chart[len(chart) - 1][1]
    for point in chart:
        result.append([width - point[0], height - point[1]])
    return result

# flips a chart
def flip(chart, flip_type):
    if flip_type == FLIP_V:
        return flip_v(chart)
    if flip_type == FLIP_H:
        return flip_h(chart)
    if flip_type == FLIP_V_AND_H:
        return flip_v_and_h(chart)
    # no flip
    return chart


def get_width(chart):
    begin = chart[0][0]
    end = chart[len(chart) - 1][0]
    return max(begin, end)


def get_height(chart):
    begin = chart[0][1]
    end = chart[len(chart) - 1][1]
    return max(begin, end)

# returns a list of starting positions from where a chart can fit in the puzzle area
def get_possible_starts(chart):
    possible_starts = list()

    chart_width = get_width(chart) 
    chart_height = get_height(chart) 

    for i in range(WIDTH - chart_width):
        for j in range(HEIGHT - chart_height):
            if fits(chart, i, j):
                possible_starts.append([i, j])

    return possible_starts

# Successively tries positioning for a combination of the four charts on all their possible positions until a solution fits for the 3 charts
# A combination of charts is defined by :
#    - the order of addition of the charts in the puzzle area
#    - the flip type of each chart (riginal, flip_vertical, flip_horizontal, flip_vertical_and_horizontal)
def try_combination(chart_1, chart_2, chart_3, chart_4, color1, color2, color3, color4):
    global nb_positioning_1, nb_positioning_2, nb_positioning_3, nb_positioning_4
    # Gets the list of possible start positions for the 1st chart and try them all:
    first_chart_starts = get_possible_starts(chart_1)
    for start_1 in first_chart_starts:
        nb_positioning_1 += 1
        put(chart_1, start_1[0], start_1[1], color1)
        # Gets the list of possible start positions for the 2nd chart and try them all:
        second_chart_starts = get_possible_starts(chart_2)
        for start_2 in second_chart_starts:
            nb_positioning_2 += 1
            put(chart_2, start_2[0], start_2[1], color2)
            # Gets the list of possible start positions for the 3rd chart and try them all:
            third_chart_starts = get_possible_starts(chart_3)
            for start_3 in third_chart_starts:
                nb_positioning_3 += 1
                put(chart_3, start_3[0], start_3[1], color3)
                # Gets the list of possible start positions for the 4th chart and try them all:
                fourth_chart_starts = get_possible_starts(chart_4)
                if len(fourth_chart_starts) > 0:
                    for start_4 in fourth_chart_starts:
                        nb_positioning_4 += 1
                        put(chart_4, start_4[0], start_4[1], color4)
                        print("SUCCESS !!!")
                        draw_grid()
                delete(chart_3, start_3[0], start_3[1])
            delete(chart_2, start_2[0], start_2[1])
        delete(chart_1, start_1[0], start_1[1])

# tries positioning all combinations for the charts (order and flip mode)
def brute_force():
    nb_tries = 0

    for a in range(len(charts)):
        key_a = list(charts.keys())[a]
        for flip_a in range(4):
            chart_a = flip(charts.get(key_a), flip_a)
            for b in range(len(charts)):
                if b != a:
                    key_b = list(charts.keys())[b]
                    for flip_b in range(4):
                        chart_b = flip(charts.get(key_b), flip_b)
                        for c in range(len(charts)):
                            if c != a and c != b:
                                key_c = list(charts.keys())[c]
                                for flip_c in range(4):
                                    chart_c = flip(charts.get(key_c), flip_c)
                                    for d in range(len(charts)):
                                        if d != a and d != b and d != c:
                                            key_d = list(charts.keys())[d]
                                            for flip_d in range(4):
                                                chart_d = flip(
                                                    charts.get(key_d), flip_d
                                                )
                                                
                                                try_combination(
                                                    chart_a,
                                                    chart_b,
                                                    chart_c,
                                                    chart_d,
                                                    key_a[0],
                                                    key_b[0],
                                                    key_c[0],
                                                    key_d[0],
                                                )
                                                
                                                nb_tries += 1

    print(f"tested the {nb_tries} possible combinations")
    print(f"tried {nb_positioning_1} positions for the first chart")
    print(f"tried {nb_positioning_2} positions for the second chart")
    print(f"tried {nb_positioning_3} positions for the third chart")
    print(f"tried {nb_positioning_4} positions for the fourth chart")


grid = init_grid()
brute_force()


def test():
    grid = init_grid()
    put(flip_v_and_h(striped_chart), 0, 6, "s")
    put(yellow_chart, 1, 0, "y")
    put(red_chart, 5, 2, "r")
    put(brown_chart, 3, 0, "b")
    draw_grid()
