
class UserStorage:

    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def numberOfUsers(self):
        return len(self.users)

    def getUserByID(self, userID):
        for user in self.users:
            if user.userID == userID:
                return user
