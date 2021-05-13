"""
File: draw_line
Name: Jasmine Tsai
-------------------------
TODO:
The first click: a small circle appears
Second click: A line appears at the clicked place
and this line is connected to the small circle for the first click.
, but the circle disappears.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the hole
SIZE = 10


window = GWindow()
# circle on canvas
is_on_c = False
old_x = 0
old_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(punch)


def punch(e):
    global is_on_c, old_x, old_y
    hole = GOval(SIZE, SIZE, x=e.x - SIZE / 2, y=e.y - SIZE / 2)
    hole.filled = True
    hole.fill_color = 'white'
    if not is_on_c:
        # get the position of the hole
        old_x = e.x
        old_y = e.y
        window.add(hole)
        is_on_c = True

    else:
        r_hole = window.get_object_at(old_x, old_y)
        line = GLine(old_x, old_y, e.x, e.y)
        window.remove(r_hole)
        window.add(line)
        is_on_c = False


if __name__ == "__main__":
    main()
