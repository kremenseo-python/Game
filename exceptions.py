"""file with exception"""


class GameOver(Exception):

    @staticmethod
    def save_result(name, score):
        with open('scores.txt', 'a') as fp:
            fp.write(f"Name: {name}, Score: {score} \n")
            fp.close()


class EnemyDown(Exception):
    pass
