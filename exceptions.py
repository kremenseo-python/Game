

class GameOver(Exception):
    pass

    @staticmethod
    def save_result(name, score):
        f = open('scores.txt', 'a')
        f.write(f"Name: {name}, Score: {score} \n")
        f.close()


# TODO расписать исключения


class EnemyDown(Exception):
    pass
