
class User:

    def __init__(self, userID, name):
        self.userID = userID
        self.name = name

    def changeName(self, newName):
        self.name = newName

    def displayUserInfo(self):
        return self.userID+self.name
