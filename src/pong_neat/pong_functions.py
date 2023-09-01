import pygame
import pickle
import neat
import os

from .pong_game import PongGame


def run_neat(
        checkpoint_path,
        draw_score,
        draw_hits,
        number_of_generations,
        pong_config,
        neat_config_path
):
    neat_config = neat.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            neat_config_path
    )

    if checkpoint_path:
        p = neat.Checkpointer.restore_checkpoint(checkpoint_path)
    else:
        p = neat.Population(neat_config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    def eval_genomes(genomes, neat_config):
        window = pygame.display.set_mode(
                (pong_config.WINDOW_WIDTH, pong_config.WINDOW_HEIGHT)
        )

        for i, (genome_id1, genome1) in enumerate(genomes):
            if i == len(genomes) - 1:
                break

            genome1.fitness = 0
            for genome_id2, genome2 in genomes[i + 1:]:
                genome2.fitness = 0 if genome2.fitness is None else \
                    genome2.fitness
                game = PongGame(pong_config, window)
                game.train_ai(
                        genome1,
                        genome2,
                        neat_config,
                        draw_score,
                        draw_hits
                )

        pygame.quit()

    winner = p.run(eval_genomes, number_of_generations)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def play_ai(ai_path, pong_config, neat_config_path):
    with open(ai_path, "rb") as f:
        winner = pickle.load(f)

    neat_config = neat.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            neat_config_path
    )

    window = pygame.display.set_mode(
            (pong_config.WINDOW_WIDTH, pong_config.WINDOW_HEIGHT)
    )
    game = PongGame(pong_config, window)
    game.play_vs_ai(winner, neat_config)


def player_vs_player(pong_config):
    window = pygame.display.set_mode(
            (pong_config.WINDOW_WIDTH, pong_config.WINDOW_HEIGHT)
    )
    game = PongGame(pong_config, window)
    game.player_vs_player()
