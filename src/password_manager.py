from user_entry import user_entry
from list_secrets import list_user_secrets
from retrieve_secret import retrieve_secret
from delete_secret import delete_secret


def user_input_check():
    try:
        user_entry()
    except TypeError:
        print('A secret with the specified name already exists')
        return user_input_check()


def user_input_prompt():
    user_input = input(
        'Please specify \033[33m[e]\033[0mntry, \033[33m[r]\033[0metrieval, \033[33m[d]\033[0meletion, \033[33m[l]\033[0misting or e\033[33m[x]\033[0mit: \n')

    if user_input == 'e':
        user_input_check()
    elif user_input == 'r':
        try:
            retrieve_secret()
        except TypeError:
            print('\nSecrets Manager can\'t find the specified secret\n')
        except AttributeError:
            print('Please enter a valid secret...\n')
    elif user_input == 'd':
        try:
            delete_secret()
        except TypeError:
            print('\nSecrets Manager can\'t find the specified secret\n')
        except AttributeError:
            print('\nPlease enter a valid secret...\n')
    elif user_input == 'l':
        list_user_secrets()
    elif user_input == 'x':
        print('\nThank you. Goodbye.')
        return
    else:
        print('Invalid input')
    user_input_prompt()


user_input_prompt()
