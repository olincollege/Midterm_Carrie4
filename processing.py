"""
Establishes a set of functions needed to process data into more helpful formats.
"""

import datetime as dt

def convert_date_to_datetime(date):
    """
    """

    date = str(date)

    no_comma_date = date.replace(",", "")

    date = dt.datetime.strptime(no_comma_date, "%B %d %Y")

    return date