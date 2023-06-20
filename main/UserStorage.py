
class UserStorage:

    def __init__(self):
        self.users = []

    def addUser(self, user):
        user.assignID(self.generateIdForNewUser())
        self.users.append(user)

    def numberOfUsers(self):
        return len(self.users)

    def getUserByID(self, userID):
        for user in self.users:
            if user.userID == userID:
                return user

    def generateIdForNewUser(self):
        if len(self.users) == 0:
            return 1
        else:
            return len(self.users)+1
