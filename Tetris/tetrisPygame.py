import pygame as py
import random as rand

py.font.init()

# GLOBALS
screen_width = 800
screen_height = 700
box_width = 300
box_height = 600
block_size = 30

x_coord = (screen_width - box_width) // 2
y_coord = screen_height - box_height

# SHAPES
# displays them in all their possible orientations
S = [
    [".....", ".....", "..00.", ".00..", "....."],
    [".....", "..0..", "..00.", "...0.", "....."],
]

Z = [
    [".....", ".....", ".00..", "..00.", "....."],
    [".....", "..0..", ".00..", ".0...", "....."],
]

I = [
    ["..0..", "..0..", "..0..", "..0..", "....."],
    [".....", "0000.", ".....", ".....", "....."],
]

O = [[".....", ".....", ".00..", ".00..", "....."]]

J = [
    [".....", ".0...", ".000.", ".....", "....."],
    [".....", "..00.", "..0..", "..0..", "....."],
    [".....", ".....", ".000.", "...0.", "....."],
    [".....", "..0..", "..0..", ".00..", "....."],
]

L = [
    [".....", "...0.", ".000.", ".....", "....."],
    [".....", "..0..", "..0..", "..00.", "....."],
    [".....", ".....", ".000.", ".0...", "....."],
    [".....", ".00..", "..0..", "..0..", "....."],
]

T = [
    [".....", "..0..", ".000.", ".....", "....."],
    [".....", "..0..", "..00.", "..0..", "....."],
    [".....", ".....", ".000.", "..0..", "....."],
    [".....", "..0..", ".00..", "..0..", "....."],
]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [
    (0, 255, 0),
    (255, 0, 0),
    (0, 255, 255),
    (255, 255, 0),
    (255, 165, 0),
    (0, 0, 255),
    (128, 0, 128),
]


# piece class that represents each moving piece
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# draws pygame screen with title
def draw_window(surface, grid):
    surface.fill((0, 0, 0))

    font = py.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))
    surface.blit(label, (x_coord + (box_width / 2) - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            py.draw.rect(
                surface,
                grid[i][j],
                (
                    x_coord + (j * block_size),
                    y_coord + (i * block_size),
                    block_size,
                    block_size,
                ),
                0,
            )

    draw_grid(surface, grid)
    py.draw.rect(surface, (255, 0, 0), (x_coord, y_coord, box_width, box_height), 4)


# formats pygame screen with grid area
def draw_grid(surface, grid):
    for i in range(len(grid)):
        py.draw.line(
            surface,
            (128, 128, 128),
            (x_coord, y_coord + i * block_size),
            (x_coord + box_width, y_coord + i * block_size),
        )
        for j in range(len(grid[i])):
            py.draw.line(
                surface,
                (128, 128, 128),
                (x_coord + j * block_size, y_coord),
                (x_coord + j * block_size, y_coord + box_height),
            )


# creates actual grid that stores the rbg values
# of tiles on the screen
def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c

    return grid


# helper function that converts shape globals
# into an array of usable coordinates
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, col in enumerate(row):
            if col == "0":
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


# checks if a move is valid on the grid
def valid_move(shape, grid):
    accepted_pos = [
        [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)
    ]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False

    return True


# helper function to check if user lost
def check_loss(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


# helper function that returns a random shape
def get_shape():
    return Piece(5, 0, rand.choice(shapes))


# displays next shape on the side of the screen
def draw_next_shape(shape, surface):
    font = py.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))

    sx = x_coord + box_width + 50
    sy = y_coord + box_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                py.draw.rect(
                    surface,
                    shape.color,
                    (sx + j * block_size, sy + i * block_size, block_size, block_size),
                    0,
                )

    surface.blit(label, (sx + 10, sy - 30))


# helper function that clears a filled row
# and moves the row above down
def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


# main run function
def run(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    run = True
    clock = py.time.Clock()
    change_piece = False
    curr_piece = get_shape()
    next_piece = get_shape()
    fall_time = 0
    fall_speed = 0.27

    # main run loop
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            curr_piece.y += 1
            if not (valid_move(curr_piece, grid)) and curr_piece.y > 0:
                curr_piece.y -= 1
                change_piece = True

        # event manager
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    curr_piece.x -= 1
                    if not (valid_move(curr_piece, grid)):
                        curr_piece.x += 1
                if event.key == py.K_RIGHT:
                    curr_piece.x += 1
                    if not (valid_move(curr_piece, grid)):
                        curr_piece.x -= 1
                if event.key == py.K_UP:
                    curr_piece.y += 1
                    if not (valid_move(curr_piece, grid)):
                        curr_piece.y -= 1
                if event.key == py.K_DOWN:
                    curr_piece.rotation += 1
                    if not (valid_move(curr_piece, grid)):
                        curr_piece.rotation -= 1

        shape_pos = convert_shape_format(curr_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = curr_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = curr_piece.color
            curr_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        py.display.update()

        if check_loss(locked_positions):
            run = False

    py.display.quit()


def main_menu(win):
    run(win)


win = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Tetris")
main_menu(win)
