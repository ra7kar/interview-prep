# Convert time from 12 hours format am/pm to military time 24 hours format.


def convert_time(t):

    am_pm = t[-2:]

    hours = int(t[:2])

    if am_pm == "AM":

        if hours == 12:
            hours = "00"

        convert_time = str(hours).rjust(2, "0") + t[2:-3]
        return convert_time

    if am_pm == "PM":

        if hours == 12:
            convert_time = str(hours) + t[2:-3]
            return convert_time

        if hours < 12:
            hours += 12
            convert_time = str(hours) + t[2:-3]
            return convert_time


# --------------
def main():
    t = "12:01:00 AM"

    ret_val = convert_time(t)
    print(ret_val)


if __name__ == "__main__":
    main()
