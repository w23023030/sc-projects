"""
File: bouncing_ball
Name: Jasmine Tsai
-------------------------
TODO:
A bouncing ball game that can be played three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
switch = False
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
out = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch
    ball.filled = True
    # click the mouse to start the game
    onmouseclicked(start)
    window.add(ball)


def start(event):
    global switch, ball, out
    vy = 0
    vx = VX
    out += 1
    # the game can be played three times
    if ball.x == START_X and ball.y == START_Y and out <= 3:
        while True:
            if switch:
                vy += GRAVITY
                ball.move(vx, vy)

                if ball.y >= window.height:
                    vy *= -REDUCE

                # return to the START_X START_Y after the ball goes out
                if ball.x >= window.width:
                    window.add(ball, START_X, START_Y)
                    switch = False
                    break
            switch = True
            pause(DELAY)


if __name__ == "__main__":
    main()
