def say_hello(name):
    print("Hello dear, " + name)

say_hello("Megha")

def say_day_of_week(date):
    import datetime
    day_of_week = date.strftime("%A")
    print("Today is " + day_of_week)

# Example usage:
import datetime
today = datetime.datetime.now()
say_day_of_week(today)
