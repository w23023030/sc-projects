"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
Create all the objects needed for the game, and then let the game start after a mouse click.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2, (self.window.height-self.paddle.height -
                                                                               PADDLE_OFFSET))

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

        # Draw bricks
        y = BRICK_OFFSET
        for i in range(BRICK_COLS):
            x = 0
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True

                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'

                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'

                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'

                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'

                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'

                self.window.add(self.brick, x, y)
                x += BRICK_WIDTH + BRICK_SPACING
            y += BRICK_HEIGHT + BRICK_SPACING

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        if (random.random() > 0.5):
            self.__dx = -self.__dx

        # The getters
        self.vx = self.__dx
        self.vy = self.__dy

        # Initialize our mouse listeners
        self.count = BRICK_ROWS*BRICK_COLS
        self.switch = False
        onmouseclicked(self.start)
        onmousemoved(self.reset_position)

    # The ball returns to the original point after losing
    def lose(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2+1

    # The ball falls out of the window
    def dead(self):
        if self.ball.y > self.window.height:
            self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

    # Set paddle to follow the mouse but not beyond the window
    def reset_position(self, e):
        if e.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif e.x > self.window.width - PADDLE_WIDTH/2:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        else:
            self.paddle.x = e.x - PADDLE_WIDTH/2
        self.window.add(self.paddle, x=self.paddle.x, y=self.window.height-PADDLE_OFFSET)

    # Click the mouse to start the game
    def start(self, e):
        if self.ball.x == (self.window.width - self.ball.width) / 2 and self.ball.y == (
                self.window.height - self.ball.height) / 2:
            self.ball.move(self.__dx, self.__dy)




























