from models import Player
from models import Enemy
import exceptions
from exceptions import EnemyDown


def play():
    """Основная функция Play"""
    print('Enter your name: ')
    player_name = str(input())
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)
    print("Hello", player_name.title() + ", please enter command 'start' to start the game")
    command_start = str(input())
    while True:
        try:
            if command_start == "start":
                player.attack(enemy)
                print(f"Your score is {player.score}")
                print(f"Your lives is {player.lives}")
                print(f"Enemy level is {enemy.level}")
                print(f"Enemy lives is {enemy.lives}")
                print('-------------------------------------------')
                player.defence(enemy)
                print(f"Your score is {player.score}")
                print(f"Your lives is {player.lives}")
                print(f"Enemy level is {enemy.level}")
                print(f"Enemy lives is {enemy.lives}")
                print('-------------------------------------------')
            else:
                print("You entered the wrong command enter. Press 'Y' to start the program.")
        except EnemyDown:
            level += 1
            enemy = Enemy(level)
            player.score += 5
            print(f"Your score is {player.score}")
            print(f"Your lives is {player.lives}")
            print(f"Enemy level is {enemy.level}")
            print(f"Enemy lives is {enemy.lives}")


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        pass
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Unacceptable character was entered!")
        pass
    finally:
        new_game = input("WANT TO PLAY? (Y/N)   ")
        if new_game == "Y":
            play()
        elif new_game == "N":
            print('Good Bye\n')
