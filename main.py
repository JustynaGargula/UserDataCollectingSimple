import main.User as u
import main.UserStorage as uS


class Main:
    def __init__(self):
        self.users = uS.UserStorage()

    def createFirstUser(self, name):
        me = u.User(name)
        self.users.addUser(me)


def print_hi(name):
    print('Hi ' + name + '!')


if __name__ == '__main__':
    Main().createFirstUser('Justyna')
    print_hi('Justyna')




