from datetime import datetime


# calculate the difference
def calculate(user_dict):
    # get the current time
    time_now = datetime.now()

    # parse user input into a datetime object
    time_ddl = datetime.strptime(user_dict['ddl'], "%Y-%m-%d %H:%M:%S")

    # calculate the difference and return 'timedelta' object
    delta = (time_ddl - time_now)

    # each unit
    delta_days = delta.days
    delta_hours = delta.seconds // 3600
    delta_minutes = delta.seconds % 3600 // 60
    delta_seconds = delta.seconds % 60

    # output = f"\"{delta.days} days {delta_hours} hours {delta_minutes} minutes {delta_seconds} seconds\" left to finish this event!"
    output = f"\"{delta.days}d{delta_hours}h{delta_minutes}mins{delta_seconds}secs\" left"
    return output
