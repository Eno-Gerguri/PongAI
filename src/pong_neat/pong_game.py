import pygame
import neat

from pong.game import Game
from pong.paddle import Paddle


class PongGame:

    def __init__(self, pong_config, window):
        self.pong_config = pong_config
        self.game = Game(self.pong_config, window)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def _handle_net_decision(self, net, paddle_direction):
        if paddle_direction == Paddle.LEFT:
            paddle = self.left_paddle
        elif paddle_direction == Paddle.RIGHT:
            paddle = self.right_paddle

        output = net.activate(
                (paddle.y, self.ball.y, abs(paddle.x - self.ball.x))
        )
        decision = output.index(max(output))

        if decision == 0:
            pass
        elif decision == 1:
            self.game.move_paddle(paddle_direction, Paddle.UP)
        else:
            self.game.move_paddle(paddle_direction, Paddle.DOWN)

    def train_ai(self, genome1, genome2, neat_config, draw_score, draw_hits):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, neat_config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, neat_config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self._handle_net_decision(net1, Paddle.LEFT)
            self._handle_net_decision(net2, Paddle.RIGHT)

            game_info = self.game.loop()
            if draw_score or draw_hits:
                self.game.draw(draw_score, draw_hits)
                pygame.display.update()

            if game_info.left_score >= 1 \
                    or game_info.right_score >= 1 \
                    or game_info.left_hits >= 50:
                self.calculate_fitness(genome1, genome2, game_info)
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome1.fitness += game_info.left_score
        genome2.fitness += game_info.right_hits
        genome2.fitness += game_info.right_score

    def play_vs_ai(self, genome, neat_config):
        net = neat.nn.FeedForwardNetwork.create(genome, neat_config)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.pong_config.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(Paddle.LEFT, Paddle.UP)
            if keys[pygame.K_s]:
                self.game.move_paddle(Paddle.LEFT, Paddle.DOWN)

            self._handle_net_decision(net, Paddle.RIGHT)

            self.game.loop()
            self.game.draw()
            pygame.display.update()

        pygame.quit()

    def player_vs_player(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(self.pong_config.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.game.move_paddle(Paddle.LEFT, Paddle.UP)
            if keys[pygame.K_s]:
                self.game.move_paddle(Paddle.LEFT, Paddle.DOWN)

            if keys[pygame.K_UP]:
                self.game.move_paddle(Paddle.RIGHT, Paddle.UP)
            if keys[pygame.K_DOWN]:
                self.game.move_paddle(Paddle.RIGHT, Paddle.DOWN)

            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()

            # Checking if someone won the game
            if game_info.left_score >= self.pong_config.WINNING_SCORE \
                or game_info.right_score >= self.pong_config.WINNING_SCORE:
                self.game.reset()

        pygame.quit()
