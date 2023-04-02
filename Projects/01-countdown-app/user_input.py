from format_output import padding


def read_user_event(user_dict):
    text = "Enter Your Event:"
    width = len(text) + 2 * padding
    prompt = f"{' ' * padding}{text}{' ' * padding}".center(width)
    return user_input_read(prompt, "event", user_dict)


def read_user_deadline(user_dict):
    return user_input_read("Enter Your Deadline (YYYY-MM-DD HH:MM:SS): ", "ddl", user_dict)


def user_input_read(prompt, key, user_dict):
    user_input = input(prompt)
    if user_input != 'exit':
        user_dict[key] = user_input
        return True
    else:
        print("Program execution completed. See you next time!")
        return False
