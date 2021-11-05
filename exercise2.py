user_email = input("Please enter a e-mail: ")


def check_email():
    if "@" in user_email and "." in user_email:
        print("Your email is valid")
    else:
        print("Your email is invalid")


check_email()
