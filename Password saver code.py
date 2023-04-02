mode = input("Would you like to add a new password or view existing ones(view,add)? press q to quit: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)


def add():
    name = input("Account name: ")
    if name == "q":
        quit()
    pwd = input("Password: ")
    if pwd == "q":
        quit()

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:

    if mode == "q":
        break

    elif mode == "view":
        view()
        break
    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        break
