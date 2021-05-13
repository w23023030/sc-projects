"""
File: my_drawing
Name: Jasmine Tsai
----------------------
TODO:
Use some triangles, squares and lines to form snoopy's home.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    Create a window and put all the shapes and lines on the canvas.
    """
    window = GWindow(500, 700, title='Snoopy\'s Home')

    rect0 = GRect(500, 700)
    rect0.filled = True
    rect0.fill_color = 'azure'
    rect0.color = 'azure'
    window.add(rect0)

    grass = GOval(600, 300)
    grass.filled = True
    grass.fill_color = 'green'
    grass.color = 'green'
    window.add(grass, -50, 630)

    rect1 = GRect(240, 200)
    rect1.filled = True
    rect1.fill_color = 'red'
    rect1.color = 'red'
    window.add(rect1, 130, 300)

    rect2 = GRect(300, 20)
    rect2.filled = True
    rect2.fill_color = 'red'
    rect2.color = 'red'
    window.add(rect2, 100, 500)

    rect3 = GRect(200, 130)
    rect3.filled = True
    rect3.fill_color = 'red'
    window.add(rect3, 150, 520)

    triangle1 = GPolygon()
    triangle1.add_vertex((130, 300))
    triangle1.add_vertex((130, 500))
    triangle1.add_vertex((80, 500))
    triangle1.color = 'red'
    window.add(triangle1)
    triangle1.filled = True
    triangle1.fill_color = 'red'

    triangle2 = GPolygon()
    triangle2.add_vertex((370, 300))
    triangle2.add_vertex((370, 500))
    triangle2.add_vertex((420, 500))
    triangle2.color = 'red'
    window.add(triangle2)
    triangle2.filled = True
    triangle2.fill_color = 'red'

    triangle3 = GPolygon()
    triangle3.add_vertex((80, 500))
    triangle3.add_vertex((100, 500))
    triangle3.add_vertex((100, 520))
    triangle3.color = 'red'
    window.add(triangle3)
    triangle3.filled = True
    triangle3.fill_color = 'red'

    triangle4 = GPolygon()
    triangle4.add_vertex((400, 500))
    triangle4.add_vertex((420, 500))
    triangle4.add_vertex((400, 520))
    triangle4.color = 'red'
    window.add(triangle4)
    triangle4.filled = True
    triangle4.fill_color = 'red'

    rect4 = GRect(250, 2)
    rect4.filled = True
    window.add(rect4, 125, 366)

    rect5 = GRect(280, 2)
    rect5.filled = True
    window.add(rect5, 110, 432)

    rect6 = GRect(180, 2)
    rect6.filled = True
    window.add(rect6, 160, 563)

    rect7 = GRect(180, 2)
    rect7.filled = True
    window.add(rect7, 160, 606)

    l1 = GLine(130, 300, 80, 500)
    window.add(l1)

    l2 = GLine(129, 300, 79, 500)
    window.add(l2)

    l3 = GLine(370, 300, 420, 500)
    window.add(l3)

    l4 = GLine(371, 300, 421, 500)
    window.add(l4)

    l5 = GLine(129, 300, 371, 300)
    window.add(l5)

    l6 = GLine(129, 299, 371, 299)
    window.add(l6)

    l7 = GLine(79, 500, 421, 500)
    window.add(l7)

    l8 = GLine(79, 501, 421, 501)
    window.add(l8)

    l9 = GLine(80, 500, 100, 520)
    window.add(l9)

    l10 = GLine(79, 501, 99, 521)
    window.add(l10)

    l11 = GLine(420, 500, 400, 520)
    window.add(l11)

    l12 = GLine(421, 501, 401, 521)
    window.add(l12)

    l13 = GLine(99, 520, 401, 520)
    window.add(l13)

    l14 = GLine(99, 521, 401, 521)
    window.add(l14)

    rl1 = GLine(149, 520, 149, 650)
    window.add(rl1)

    rl2 = GLine(351, 520, 351, 650)
    window.add(rl2)

    rl3 = GLine(149, 651, 351, 651)
    window.add(rl3)

    label = GLabel('Snoopy\'s Home')
    label.color = 'navy'
    label.font = 'Times New Roman-40-Bold'
    window.add(label, 120, 90)


if __name__ == '__main__':
    main()
