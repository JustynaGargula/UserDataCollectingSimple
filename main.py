import main.User as u
import main.UserStorage as uS


class Main:
    def __init__(self):
        self.users = uS.UserStorage()

    def createUser(self, name):
        me = u.User(name)
        self.users.addUser(me)
        print("Information about user: ", me.displayUserInfo())


def print_hi(name):
    print('Hi ' + name + '!')


if __name__ == '__main__':
    m = Main()
    m.createUser('Justyna')
    print_hi('Justyna')


