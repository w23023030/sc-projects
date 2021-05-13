"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
When the ball hits a brick, the brick will disappear, and the ball will bounce when it hits the paddle.
And this game can be played NUM_LIVES times.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    count = 0
    live = NUM_LIVES
    while live > 0:
        if graphics.ball.x != (graphics.window.width - graphics.ball.width) / 2 and graphics.ball.y != (
                graphics.window.height - graphics.ball.height) / 2:
            graphics.ball.move(graphics.vx, graphics.vy)

            if graphics.ball.x == (graphics.window.width - graphics.ball.width) / 2 or graphics.ball.y == (
                    graphics.window.height - graphics.ball.height) / 2:
                graphics.ball.move(graphics.vx, graphics.vy)
            # The ball must be inside the window
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.vx = -graphics.vx
            if graphics.ball.y <= 0:
                graphics.vy = -graphics.vy

            # When the ball falls
            graphics.dead()

            p1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            p2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            p3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.width)
            p4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.width)

            # Check if there are any objects in the four corners
            if p1 is not None:
                if graphics.ball.y > graphics.window.height/2:
                    graphics.vy = -graphics.vy
                else:
                    graphics.window.remove(p1)
                    count += 1
                    graphics.vy = -graphics.vy

            elif p2 is not None:
                if graphics.ball.y > graphics.window.height / 2:
                    graphics.vy = -graphics.vy
                else:
                    graphics.window.remove(p2)
                    count += 1
                    graphics.vy = -graphics.vy

            elif p3 is not None:
                if graphics.ball.y > graphics.window.height / 2:
                    graphics.vy = -graphics.vy
                else:
                    graphics.window.remove(p3)
                    count += 1
                    graphics.vy = -graphics.vy

            elif p4 is not None:
                if graphics.ball.y > graphics.window.height / 2:
                    graphics.vy = -graphics.vy
                else:
                    graphics.window.remove(p4)
                    count += 1
                    graphics.vy = -graphics.vy

        pause(FRAME_RATE)

        # When the ball falls once, it loses one life
        if graphics.ball.y >= graphics.window.height-10:
            live -= 1
            # The ball falls below three times
            if live == 0:
                graphics.lose()
                break

        # All bricks have been removed
        elif count == graphics.count:
            graphics.lose()
            break


if __name__ == '__main__':
    main()
