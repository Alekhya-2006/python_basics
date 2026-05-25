# OOP Chat System
# Concepts:
# Classes, Objects, Composition,
# Lists, Dictionaries, Menu System


class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        User.total_users += 1


class Message:

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content


class ChatRoom:

    def __init__(self):

        self.users = []
        self.messages = []


    # Join

    def join_user(self, user):

        if user not in self.users:
            self.users.append(user)

            print(f"{user.username} joined chat")

        else:
            print("User already exists")
    
    # Leave

    def remove_user(self, user):

        if user in self.users:

            self.users.remove(user)

            print(f"{user.username} left chat")

        else:
            print("User not found")

    # Send Message

    def send_message(self, sender, content):

        if sender not in self.users:

            print("User not in chat room")
            return


        message = Message(sender, content)

        self.messages.append(message)

        print("Message Sent")

    # History

    def show_chat_history(self):

        print("\n--- Chat History ---")

        if len(self.messages) == 0:

            print("No Messages")

        else:

            for message in self.messages:

                print(
                    f"{message.sender.username}: "
                    f"{message.content}"
                )

    # Active Users

    def show_active_users(self):

        print("\n--- Active Users ---")

        if len(self.users) == 0:

            print("No Active Users")

        else:

            for user in self.users:

                print(user.username)


room = ChatRoom()

registered_users = {}


while True:

    print("\n1. Join")
    print("2. Leave")
    print("3. Send Message")
    print("4. Chat History")
    print("5. Active Users")
    print("6. Exit")

    choice = int(input("Choose (1-6): "))


    if choice == 6:

        print("Exited")

        break


    elif choice == 1:

        username = input("Enter Username: ")

        user = User(username)

        registered_users[username] = user

        room.join_user(user)


    elif choice == 2:

        username = input("Username: ")

        if username in registered_users:

            room.remove_user(
                registered_users[username]
            )

        else:
            print("User not found")


    elif choice == 3:

        username = input("Username: ")

        msg = input("Message: ")


        if username in registered_users:

            room.send_message(
                registered_users[username],
                msg
            )

        else:
            print("User not found")


    elif choice == 4:

        room.show_chat_history()


    elif choice == 5:

        room.show_active_users()


    else:

        print("Invalid Choice")             