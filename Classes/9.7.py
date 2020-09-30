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


class Admin(User):
    def __init__(self, first_name, last_name, identificator, nick, priviledges):
        super().__init__(first_name, last_name, identificator, nick)
        self.privileges = Priviledges(priviledges)


class Priviledges:
    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        for priviledge in self.priviledges:
            print('Access to: ' + priviledge)


admin1 = Admin('Bartosz', 'Chojnacki', '34r', 'Bart', ['Read', 'Write', 'Modify'])
admin1.privileges.show_priviledges()

