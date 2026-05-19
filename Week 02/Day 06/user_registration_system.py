# User Registration System
# Concept: @classmethod

class User:
    total_users = 0
    
    def __init__(self, username):
        User.total_users += 1
        self.username = username

    @classmethod
    def user_count(cls):
        return cls.total_users
    
user1 = User("Alekhya")
user2 = User("Sam")
user3 = User("John")

print("Total Users =", User.user_count())