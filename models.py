import random
from exceptions import EnemyDown
from exceptions import GameOver


class Enemy:

    def __init__(self, level):
        """Инициализируем уровень противника"""
        self.lives = level
        self.level = level

    @staticmethod
    def select_attack():
        """Возвращает рандомное значение"""
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()
        return self.lives


class Player:
    score = None
    lives = 3
    allowed_attacs = None

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def fight(attack, defence):
        result = None
        return result

    def attack(self, enemy_obj):
        command_start = str(input())
        if command_start == "START":
            print(str("Choose your HERO: 1 - MAG, 2 - WARRIOR, 3 - ROGUE"))
        move = int(input())

        # if hero == 1:
        #     return 'Your Choose MAG, Goog luck!'
        # elif hero == 2:
        #     return "YEAH, It's WARRIOR!!"
        # elif hero == 3:
        #     return "FUCK, You are ROGUE, be careful"



    def defence(self):
        pass

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()
        return self.lives


dima = Player(5)
