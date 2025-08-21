from datetime import timedelta

YEAR = 365

def format_duration(seconds):
    if seconds <= 0:
        return "now"

    td = timedelta(seconds=seconds)
    dur_array = []

    years = int(td.days / YEAR)
    if 0 < years:
        dur_array.append(f"{years} year{'s' if 1 < years else ''}")

    days = td.days - years * YEAR
    if 0 < days:
        dur_array.append(f"{days} day{'s' if 1 < days else ''}")

    if 0 < years or 0 < days:
        hours_min_sec = str(td).split()[2]
    else:
        hours_min_sec = str(td)

    hours = int(hours_min_sec.split(':')[0])
    if 0 < hours:
        dur_array.append(f"{hours} hour{'s' if 1 < hours else ''}")

    minutes = int(hours_min_sec.split(':')[1])
    if 0 < minutes:
        dur_array.append(f"{minutes} minute{'s' if 1 < minutes else ''}")

    seconds = int(hours_min_sec.split(':')[2])
    if 0 < seconds:
        dur_array.append(f"{seconds} second{'s' if 1 < seconds else ''}")

    res = dur_array[0]
    if 1 < len(dur_array):
        for i in range(1, len(dur_array)):
            if i < len(dur_array)-1:
                res += f", {dur_array[i]}"
            else:
                res += f" and {dur_array[i]}"

    return res


if __name__ == '__main__':
    print(format_duration(253374061)) #"8 years, 12 days, 13 hours, 41 minutes and 1 second"
    print(format_duration(3662)) #"1 hour, 1 minute and 2 seconds"
    print(format_duration(15731080)) #"182 days, 1 hour, 44 minutes and 40 seconds"
    print(format_duration(62)) #"1 minute and 2 seconds"