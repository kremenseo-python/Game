from models import Player
from models import Enemy
import exceptions


def play():
    """Основная функция Play"""
    print('Enter your name: ')
    player_name = str(input())
    player = Player(player_name)
    level = 1
    enemy = Enemy(level=1)
    print("Hello", player_name.title() + ", please enter command 'START' to start the game")
    command_start = str(input())

    if command_start == "START":
        while player.lives > 0:
            player.attack(enemy)

            if enemy.lives == 0:
                level += 1
                enemy = Enemy(level)
                player.score += 5
            print(f"Your score is {player.score}")
            print(f"Your lives is {player.lives}")
            print(f"Enemy level is {enemy.level}")
            print(f"Enemy lives is {enemy.lives}")
            print('-------------------------------------------\n'
                  '-------------------------------------------\n'
                  '-------------------------------------------')

            player.defence(enemy)
            print(f"Your score is {player.score}")
            print(f"Your lives is {player.lives}")
            print(f"Enemy level is {enemy.level}")
            print(f"Enemy lives is {enemy.lives}")
            print('-------------------------------------------\n'
                  '-------------------------------------------\n'
                  '-------------------------------------------')


if __name__ == '__main__':
    result = None
    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        new_game = input("WANT TO PLAY? (Y/N)   ")
        if new_game == "Y":
            play()
        elif new_game == "N":
            print('Good Bye')