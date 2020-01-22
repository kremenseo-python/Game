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
        if not self.lives:
            raise EnemyDown()


class Player:

    def __init__(self, player_name, score=0, lives=5):
        self.player_name = player_name
        self.score = score
        self.lives = lives

    @staticmethod
    def fight(attack, defense):
        result = None
        if attack == defense:
            result = 0
        elif attack == 2 and defense == 1:
            print('Win MAG')
            result = -1
        elif attack == 3 and defense == 2:
            print('Win WARRIOR')
            result = -1
        elif attack == 1 and defense == 3:
            print('Win ROGUE')
            result = -1
        elif attack == 1 and defense == 2:
            print('Win MAG')
            result = 1
        elif attack == 2 and defense == 3:
            print('Win WARRIOR')
            result = 1
        elif attack == 3 and defense == 1:
            print('Win ROGUE')
            result = 1
        return result

    def decrease_lives(self):
        """Метод отнимающий жизни"""
        self.lives -= 1
        if self.lives == 0:
            print('Your Game is Over')
            print('Your total score is ', self.score)
            GameOver.save_result(self.player_name, self.score)
            raise GameOver()

    def attack(self, enemy_obj):
        print("Turn Player")
        self.choice()
        attack_player = int(input())
        attack_comp = enemy_obj.select_attack()
        print(attack_comp)
        result_fight = Player.fight(attack_player, attack_comp)
        if result_fight == 0:
            print("It's a draw!")
        elif result_fight == 1:
            print("You attacked successfully")
            enemy_obj.decrease_lives()
            self.score += 1
        elif result_fight == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        print("Turn Computer")
        self.choice()
        attack_comp = enemy_obj.select_attack()
        attack_player = int(input())
        print(attack_comp)
        result_fight = Player.fight(attack_comp, attack_player)
        if result_fight == 0:
            print("It's a draw!!!")
        elif result_fight == 1:
            print("Computer attacked was successful")
            self.decrease_lives()
        elif result_fight == -1:
            print("Enemy missed!")
            self.score += 1

    @staticmethod
    def choice():
        """Метод для выбора героя"""
        print("Choose your HERO: 1 - MAG, 2 - WARRIOR, 3 - ROGUE")
