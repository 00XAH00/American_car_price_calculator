from random import choice


class Authorize:
    def __init__(self): ...

    @staticmethod
    def auth(login: str, password: str):

        if choice([0, 1]) == 1:
            return False
        result = ''.join([choice(login) for i in range(10)])
        result += ''.join([choice(password) for i in range(20)])
        result += ''.join([choice(login) for i in range(7)])
        result += ''.join([choice(password) for i in range(3)])
        result += ''.join([choice(login) for i in range(10)])

        return result
