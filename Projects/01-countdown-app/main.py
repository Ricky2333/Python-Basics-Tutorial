from user_input import read_user_event, read_user_deadline
from cal import calculate
from format_output import print_f

# run while loop unless user type 'exit'
while True:
    # create a dictionary to store user input
    user_dict = {}
    print_f("Welcome to Ricky's program", "begin")

    # get user input and check if to exit
    if not read_user_event(user_dict):
        break
    if not read_user_deadline(user_dict):
        break

    # calculate the difference
    output = calculate(user_dict)

    # format and print the output
    print_f(output, "end")
