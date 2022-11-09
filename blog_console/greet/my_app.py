import datetime
import argparse


def get_salutation():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        return "Good Morning!"
    if current_time.hour < 18:
        return "Good Afternoon!"
    return "Good Evening!"


def my_func():
    my_greeting_str = "Hi there! " + get_salutation() + " Nice to meet you"
    print(my_greeting_str)
    return 0


def my_func_with_args():
    parser = argparse.ArgumentParser(
        prog="Greeter",
        description="Greeter - demo code for explaining console commands",
    )

    parser.add_argument(
        "-name",
        type=str,
        default=False,
        dest="name",
        help="provide your name",
    )

    args = parser.parse_args()

    if args.name:
        my_greeting_str = (
            "Hi! " + args.name + "," + get_salutation() + " Nice to meet you"
        )
    else:
        my_greeting_str = "Hi there! " + get_salutation() + " Nice to meet you"
    print(my_greeting_str)


if __name__ == "__main__":
    my_func()
