import pygame

from .paddle import Paddle
from .ball import Ball
from .game_information import GameInformation

pygame.init()


class Game:

    def __init__(self, pong_config, window):
        pygame.init()
        self.pong_config = pong_config
        self.window = window
        self.window_width, self.window_height = pygame.display \
            .get_surface().get_size()

        self.left_paddle = Paddle(
                x=10,
                y=self.window_height // 2 -
                  self.pong_config.PADDLE_HEIGHT // 2,
                width=self.pong_config.PADDLE_WIDTH,
                height=self.pong_config.PADDLE_HEIGHT,
                color=self.pong_config.PRIMARY_COLOR,
                vel=self.pong_config.PADDLE_VELOCITY
        )
        self.right_paddle = Paddle(
                x=self.window_width - 10 - self.pong_config.PADDLE_WIDTH,
                y=self.window_height // 2 -
                  self.pong_config.PADDLE_HEIGHT // 2,
                width=self.pong_config.PADDLE_WIDTH,
                height=self.pong_config.PADDLE_HEIGHT,
                color=self.pong_config.PRIMARY_COLOR,
                vel=self.pong_config.PADDLE_VELOCITY
        )
        self.ball = Ball(
                x=self.window_width // 2,
                y=self.window_height // 2,
                radius=self.pong_config.BALL_RADIUS,
                color=self.pong_config.PRIMARY_COLOR,
                max_vel=self.pong_config.BALL_MAXIMUM_VELOCITY
        )

        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0

    def _draw_score(self):
        left_score_text = self.pong_config.SCORE_FONT.render(
            str(self.left_score), 1, self.pong_config.PRIMARY_COLOR
        )
        right_score_text = self.pong_config.SCORE_FONT.render(
            str(self.right_score), 1, self.pong_config.PRIMARY_COLOR
        )

        self.window.blit(
            left_score_text,
            (self.window_width // 4 - left_score_text.get_width() // 2, 20)
        )
        self.window.blit(
            right_score_text,
            (
                3 * self.window_width // 4 - right_score_text.get_width() // 2,
                20
            )
        )

    def _draw_hits(self):
        hits_text = self.pong_config.HITS_FONT.render(
                str(self.left_hits + self.right_hits),
                1,
                self.pong_config.SECONDARY_COLOR
        )

        self.window.blit(
                hits_text,
                (self.window_width // 2 - hits_text.get_width() // 2, 10)
        )

    def _draw_divider(self):
        for i in range(10, self.window_height, self.window_height // 20):
            if i % 2 == 1:
                continue

            pygame.draw.rect(
                self.window, self.pong_config.PRIMARY_COLOR,
                (self.window_width // 2 - 5, i, 10, self.window_height // 20)
            )

    def _handle_collision(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle
        pong_config = self.pong_config

        if ball.y + pong_config.BALL_RADIUS >= self.window_height \
            or ball.y - pong_config.BALL_RADIUS <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            if left_paddle.y <= ball.y <= \
                    left_paddle.y + pong_config.PADDLE_HEIGHT \
                    and ball.x - pong_config.BALL_RADIUS \
                        <= left_paddle.x + pong_config.PADDLE_WIDTH:
                ball.x_vel *= -1

                middle_y = left_paddle.y + pong_config.PADDLE_HEIGHT / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = pong_config.PADDLE_HEIGHT / 2 / \
                                    pong_config.BALL_MAXIMUM_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
                self.left_hits += 1

        else:
            if right_paddle.y <= ball.y <= \
                    right_paddle.y + pong_config.PADDLE_HEIGHT \
                    and ball.x + pong_config.BALL_RADIUS >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + pong_config.PADDLE_HEIGHT / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = pong_config.PADDLE_HEIGHT / 2 \
                                   / pong_config.BALL_MAXIMUM_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
                self.right_hits += 1

    def draw(self, draw_score=True, draw_hits=True):
        self.window.fill(self.pong_config.BACKGROUND_COLOR)

        self._draw_divider()
        if draw_score:
            self._draw_score()
        if draw_hits:
            self._draw_hits()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.window)

        self.ball.draw(self.window)

    def move_paddle(self, left=Paddle.LEFT, up=Paddle.UP):
        if left:
            if up \
                    and self.left_paddle.y - self.pong_config.PADDLE_VELOCITY \
                        < 0:
                return False
            if not up \
                    and self.left_paddle.y + self.pong_config.PADDLE_HEIGHT \
                        > self.window_height:
                return False
            self.left_paddle.move(up)
        else:
            if up and \
                    self.right_paddle.y - self.pong_config.PADDLE_VELOCITY < 0:
                return False
            if not up \
                    and self.right_paddle.y + self.pong_config.PADDLE_HEIGHT \
                        > self.window_height:
                return False
            self.right_paddle.move(up)

        return True

    def loop(self):
        self.ball.move()
        self._handle_collision()

        if self.ball.x < 0:
            self.ball.reset()
            self.right_score += 1
        elif self.ball.x > self.window_width:
            self.ball.reset()
            self.left_score += 1

        game_info = GameInformation(self.left_hits, self.right_hits,
                                    self.left_score, self.right_score)

        return game_info

    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
