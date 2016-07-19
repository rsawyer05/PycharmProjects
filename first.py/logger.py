import logging


logging.basicConfig(filename='game.log', level=logging.debug)


# At logging location
logging.info('monster: {}, door: {} player: {}'.format(monster, door, player[location]))

