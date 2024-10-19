# Basic User Class
class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"I am {self.name} and my user name is {self.username} and contact me throught {self.email}"


ajay = User("ajay", "ajay84", "ajay8425p@gmail.com")
print(ajay)

# Insertion , Finding , Updation


class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"I am {self.name} and my user name is {self.username} and contact me throught {self.email}"


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username == user.username:
                return "Username Already Exist"
            elif self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


ajay = User("ajay", "ajay84", "ajay@gmail.com")
dhya = User("Dhya", "dhyanes", "dhya94@gmail.com")
atma = User("Atma", "atma3", "atma2@gmail.com")
atma1 = User("Atuma", "atma3", "atma444@gmail.com")
print(ajay)
database = UserDatabase()
database.insert(ajay)
database.insert(dhya)
database.insert(atma)
database.users
print(database.find("atma3"))
database.update(atma1)
print(database.list_all())

"""
Time Complexity :

Insertion : N
Finding :   N
Updation :  N
List : 1

Space Complexity : 1
"""
