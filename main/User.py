
class User:

    def __init__(self, name):
        self.userID = 0
        self.name = name

    def changeName(self, newName):
        self.name = newName

    def displayUserInfo(self):
        return str(self.userID)+" "+self.name

    def assignID(self, userID):
        self.userID = userID
