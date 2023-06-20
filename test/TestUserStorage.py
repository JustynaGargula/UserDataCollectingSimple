import unittest
from main.User import User
from main.UserStorage import UserStorage


class TestUserStorage(unittest.TestCase):

    u1 = User("Max")
    u2 = User("Diana")
    u3 = User("Alex")
    users = UserStorage()
    users.addUser(u1)
    users.addUser(u2)
    users.addUser(u3)

    def testNumberOfUsers(self):
        self.assertEqual(self.users.numberOfUsers(), 3, "Should be 3")

    def testNameOfSecondUser(self):
        foundUser = self.users.getUserByID(2)
        self.assertEqual(foundUser.name, "Diana", "Name should be Diana")

    def testIdGenerating(self):
        self.assertEqual(self.u3.userID, 3, "User ID should be 3")

