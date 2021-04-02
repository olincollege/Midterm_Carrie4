import datetime as dt

def convert_date_to_date_string(date):
    """
    """
    no_comma_date = date.replace(",", "")

    list_date = no_comma_date.split()

    month_number = dt.datetime.strptime(list_date[0], "%B")

    date_string = month_number + list_date[1] + list_date[2]

    return date_string