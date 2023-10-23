import hashlib
from colorama import Fore, Style, init
import bcrypt

init()


def print_colorful_text(text, r, g, b):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")




def print_logo():
    logo = """
    ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███    ██████  ██░ ██  ▄▄▄       ██▀███   ██ ▄█▀
▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒ ██▄█▒ 
▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ 
▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ 
▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄
░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░
░       ▒ ▒ ░░   ░    ░    ░     ░░   ░ ░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░ ░ ░░ ░ 
░ ░     ░ ░      ░         ░  ░   ░           ░   ░  ░  ░      ░  ░   ░     ░  ░   
░       ░ ░           ░                                                                            


    """
    print_colorful_text(logo, 255, 165, 0)


def welcome_message():
    print_logo()
    print_colorful_text("Welcome to CyberShark Pass00wrd-Changer!", 0, 255, 0)
    print_colorful_text("This Pass00wrd-Changer was built by CyberShark Team", 255, 0, 0)
    print()


def hash_password(password):
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash_password

def verify_password(stored_hashed_password, password):
    return bcrypt.checkpw(password.encode(), stored_hashed_password)

def change_password(username, old_password, new_password):
    print(f"Changing password for user ' {username}'....")

    stored_hashed_password = hash_password(new_password.encode())

    if verify_password(stored_hashed_password, old_password):
        if not is_weak_password(new_password):
            new_hashed_password = hash_password(new_password)

            print("Password successfully changed!")
        else:
            print("New password is too weak. Please Choose a stronger password")
    else:
        print("Old password is incorrect. Password change failed.")



def is_weak_password(password):
    return len(password) < 8

def main():
    welcome_message()
    username = input("Enter your username: ")
    old_password = input("Enter your old password: ")
    new_password = input("Enter your new password: ")


    change_password(username, old_password, new_password)

if __name__ == "__main__":
    main()




