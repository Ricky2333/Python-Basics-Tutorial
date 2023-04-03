from format_output import padding
from validate import validate_deadline


def get_user_event(user_dict):
    prompt = "Enter Your Event:"
    key = "event"
    # width = len(text) + 2 * padding
    # prompt = f"{' ' * padding}{text}{' ' * padding}".center(width)
    return get_user_input(prompt, key, user_dict)


def get_user_deadline(user_dict):
    prompt = "Enter Your Deadline (YYYY-MM-DD HH:MM:SS):"
    key = "ddl"
    while True:
        # user's input is not "exit"
        if get_user_input(prompt, key, user_dict):
            # check if user's ddl is valid
            if validate_deadline(user_dict[key]):
                return True
            else:
                print("Your input of deadline is not valid!\n")
        else:
            return False


def get_user_input(prompt, key, user_dict):
    user_input = input(prompt)
    if user_input != 'exit':
        user_dict[key] = user_input
        return True
    else:
        print("Program execution completed. See you next time!")
        return False
