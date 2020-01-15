"""Вопросы:
    1. обязателен ли файл settings.py и какие константы он должен хранить*"""

from models import Player
from models import Enemy
import exceptions


def play():
    print('Enter your name: ')
    player_name = str(input())
    player = Player(player_name)
    enemy = Enemy(level=1)
    print('Hello', player_name, "please enter command 'START' to start the game")
    player.attack(enemy)


if __name__ == '__main__':
    result = None
    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')