# Pong AI

An interface to train an AI using the NEAT algorithm, with the ability to play against the trained AI.

There is also the option to play against another human.

This application was made in python. The interface was made using `PySimpleGUI` and the Pong game made using `Pygame` and the NEAT algorithm implemented using the python package `neat`.

### How to Use This Project

##### Main Menu

![Main Menu](imgs\Main Menu.jpg)

The Main Menu is simple consisting on the user's four options:

1) **Train AI** - The user can go on to see the options on training a Pong AI
2) **Play VS AI** - The user can go on to play against a trained AI
3) **Player 1 VS Player 2** - The user can go on to play a simple Pong Game with another user on the same machine
4) **Settings** - The user can go on to pick a certain file for Pong Configurations on how they want the game to run

##### Train AI

![Train AI](imgs\Train AI.jpg)

The Train AI Menu has a few options for how the user may wish to train the AI:

1. **Draw Scores** - If toggled then when training you will see the scores of each AI
2. **Draw Hits** - If toggled  then the ball of and he paddles will be rendered so the user can see the training occur
3. **No. of Generations** - The number inputted here will be the number of generations to train the AI for before saving the best in `best.pickle`
4. **Train From Check** - Pick a file path for a checkpoint to start the training from

##### Play VS AI

![Play VS AI](imgs\Play VS AI.jpg)

The Play VS AI Menu has a way to pick a file with the AI and then starts a game against it:

1. **Play** - Will automatically pick `best.pickle` 
2. **Play Custom** - Browse a file of the AI

##### Player 1 VS Player 2

![Player VS Player](imgs\Player VS Player.jpg)

Goes straight into a game:

- The left paddle uses W and S keys

- The right paddle uses UP ARROW and DOWN ARROW keys

##### Settings

![Settings](imgs\Settings.jpg)

The Settings Menu allows the user to choose a custom pong configuration file.

Otherwise it defaults to `Pong/pong_config.json`

### The NEAT Algorithm

NeuroEvolution of Augmenting Toplogies (NEAT) is an algorithm based on the concept of evolution using evolving neural networks.

It is a type of reinforcement learning, meaning that it rewards good behaviour and then eliminates the networks, which do not perform well or respond well to that reward for a better outcome.

##### Pong Neural Network

![Pong Neural Network](imgs\Pong Neural Network.jpg)

**Input Values:** Y value of Paddle, Y value of ball, Distance between ball and paddle

**Output Values:** Stay, Up, Down

##### Fitness

The network will create different weights and biases so as to be optimised for best play.

The AI is optimised for number of hits it returns to the other player to ensure an AI that can continuously play. It is also slightly optimised for scoring by adding its score to its fitness to try and make it more offensive and go for a win.

##### What NEAT Does

The NEAT algorithm is going to create many generations of different genomes, a neural network with a predefined number of hidden layers and hidden nodes.

Over the course of generations there will be small mutations in the best performing genomes within each generation to allow for variation and potentially better networks. The process will repeat for the specified number of generations.

We determine which genomes are performing the best based on their fitness. A higher fitness means better performance.

At the end of each generation, we will discard the weakest performing ones. We will also then breed the best ones to go onto the next generation. This involves looking at their architecture, taking their properties and merging them into a new network.

Within each generation there will be a subset of different species depending on the size of each generation. This is to allow for genetic variety and also for a potential species that is bad at an earlier generation to stay alive if it has future potential.

At the end of the specified generations we select the genome with the best fitness and save it for use as we wish later.