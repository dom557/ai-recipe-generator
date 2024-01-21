import user_interface
from login_interface import LoginInterface
import json
def main():
    # Check if the user is logged in
    if check_login():
        # If logged in, proceed to the main interface
        run_user_interface()
    else:
        # If not logged in, show the login interface
        run_login_interface()



def check_login():
    # Logic to check the login status
    # Load user data from the JSON file
    with open('user.json', 'r') as file:
        data = json.load(file)

    # Check if the user is logged in
    if 'logged_in' in data and data['logged_in']:
        return True
    else:
        return False

def run_login_interface():
    # Initialize the login interface
    login_ui = LoginInterface()
    logged_in = login_ui.run()

    if logged_in:
        # Proceed to the main interface
        run_user_interface()

def run_user_interface():
    # Initialize the user interface
    ui = user_interface.UserInterface()
    ui.run()




if __name__ == '__main__':
    main()
