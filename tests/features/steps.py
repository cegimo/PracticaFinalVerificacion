from lettuce import *
from juego.game import Game


@step(u'the username is ([^\s]+) score ([^\s]+)')
def definePlayer(step, name, score):
    world.name = name
    world.score = score


@step('I create my player')
def createPLayer(step):
    game = Game()
    game.createPLayer(world.name, world.score)


@step('I can see his score')
def exitsUser(step):
    game = Game()
    print world.name
    game.seeScore(world.name)

