import os


class User:

    def login(self, username, password):
        with open("login_info.txt", 'r') as login1:
            for line1 in login1:
                _username, _password = eval(line1)
                if _username == username and _password == password:
                    print("Login successful")
                    break
            else:
                print("Username or password is wrong")

    def create_new_account(self, username: str, password: str):
        with open("login_info.txt", 'a') as login2:
            # print("{}\t{}".format(username, password), file=login)
            print((username, password), file=login2)
            print("Account created successfully")


if __name__ == '__main__':
    options = {1: "Create Account", 2: "Login", 0: 'Quit'}
    while True:
        print("Welcome to my project\n"
              "Please select the options below(0 to quit):")
        for index in options.keys():
            print(index, options[index], sep='. ')
        option = int(input())
        if option == 0:
            break
        if option == 1:
            quit_ = False
            while not quit_:
                user_name = input("Enter new username: ")
                pass_ = input("Enter a password: ")
                with open("login_info.txt", 'r') as login:
                    if os.stat("login_info.txt").st_size == 0:
                        User().create_new_account(user_name, pass_)
                        quit_ = True
                    else:
                        for line in login:
                            _name, _pass = eval(line.strip())
                            if _name == user_name:
                                print("Username already exists.\nPlease enter a new username")
                                break
                        else:
                            User().create_new_account(user_name, pass_)
                            quit_ = True
        elif option == 2:
            user_name = input("Enter your username: ")
            pass_ = input("enter your password: ")
            User().login(user_name, pass_)
        else:
            print("Invalid option")



