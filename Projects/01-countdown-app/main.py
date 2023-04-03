from get_user_input import get_user_event, get_user_deadline
from cal import calculate
from format_output import print_f
import time

# run while loop unless user type 'exit'
while True:
    # create a dictionary to store user input
    user_dict = {}

    # print prompt
    print_f("Welcome to Ricky's program", "begin")
    time.sleep(1)

    # get user input and check if to exit
    if not get_user_event(user_dict):
        break
    if not get_user_deadline(user_dict):
        break

    # calculate the difference
    output = calculate(user_dict)

    # format and print the output
    print_f(output, "end")

    time.sleep(3)
