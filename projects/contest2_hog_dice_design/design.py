from gui_files.svg import *

DICE_CAPTION = "Replace this caption with one of your own!"


def draw_dice(num):
    # **YOUR CODE HERE**
    assert(num <= 6)
    width, height = 100, 100
    graphic = create_graphic(width, height)
    draw_rect(graphic, 0, 0, 100, 100, fill="white", stroke="black")
    if num == 1:
        draw_circle(graphic, 50, 50, 10, stroke='yellow', fill='red')
    elif num == 2:
        draw_circle(graphic, 25, 50, 10, stroke='green', fill='blue')
        draw_circle(graphic, 75, 50, 10, stroke='green', fill='blue')
    elif num == 3:
        draw_triangle(graphic, 50, 28, 45, 35.5, 55, 35.5, stroke='black', fill='grey')
        draw_triangle(graphic, 33, 61, 28, 68.5, 38, 68.5, stroke='black', fill='grey')
        draw_triangle(graphic, 66, 61, 61, 68.5, 71, 68.5, stroke='black', fill='grey')
    elif num == 4:
        draw_rect(graphic, 25, 25, 10, 10, stroke='brown', fill='pink')
        draw_rect(graphic, 25, 75, 10, 10, stroke='brown', fill='pink')
        draw_rect(graphic, 75, 25, 10, 10, stroke='brown', fill='pink')
        draw_rect(graphic, 75, 75, 10, 10, stroke='brown', fill='pink')
    elif num == 5:
        draw_line(graphic, 24, 25, 76, 25, stroke='black')
        draw_line(graphic, 24, 50, 76, 50, stroke='black')
        draw_line(graphic, 24, 75, 76, 75, stroke='black')
        draw_line(graphic, 50, 25, 50, 75, stroke='black')
    else:
        draw_circle(graphic, 33, 25, 10, stroke='green', fill='blue')
        draw_circle(graphic, 66, 25, 10, stroke='green', fill='blue')
        draw_rect(graphic, 33, 50, 10, 10, stroke='brown', fill='pink')
        draw_rect(graphic, 66, 50, 10, 10, stroke='brown', fill='pink')
        draw_triangle(graphic, 33, 70, 28, 77.5, 38, 77.5, stroke='black', fill='grey')
        draw_triangle(graphic, 66, 70, 61, 77.5, 71, 77.5, stroke='black', fill='grey')
    return graphic
