class User:
    def __init__(self, first_name, last_name, identificator, nick):
        self.first_name = first_name
        self.last_name = last_name
        self.identificator = identificator
        self.nick = nick
        self.login_attempts = 0

    def describe_user(self):
        print('Your first name is: ' + self.first_name.title())
        print('Your last name is: ' + self.last_name.title())
        print('Your id is: ' + self.identificator.title())
        print('Your nick is: ' + self.nick.title())

    def greet_user(self):
        print('Hello ' + self.first_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Bartosz', 'Chojnacki', '4321', 'Bartolomeo')
user1.describe_user()
user1.greet_user()

for i in range(5):
    user1.increment_login_attempts()
    print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
