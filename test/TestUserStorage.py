import unittest
from main.User import User
from main.UserStorage import UserStorage


class TestUserStorage(unittest.TestCase):

    u1 = User(1, "Max")
    u2 = User(2, "Diana")
    u3 = User(3, "Alex")
    users = UserStorage()
    users.addUser(u1)
    users.addUser(u2)
    users.addUser(u3)

    def testNumberOfUsers(self):
        self.assertEqual(self.users.numberOfUsers(), 3, "Should be 3")

    def testNameOfSecondUser(self):
        foundUser = self.users.getUserByID(2)
        self.assertEqual(foundUser.name, "Diana", "Name should be Diana")

