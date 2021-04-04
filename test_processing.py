"""
Test functions to process the contents of a Netflix titles dataframe
"""

from collections import Counter
import pytest
import datetime

from processing import (
    remove_rows_containing_nan,
    convert_date_to_datetime,
)

remove_rows_containing_nan_cases = [
    #Check that this program works on two short lists
    ([1, None ,3], ["a", "b", None], [1], ["a"]),
    #Check that this works on lists of different lengths
    ([1, 2, 3, 4, 5], ["a", "b"], [1, 2], ["a","b"]),
]

convert_date_to_datetime_cases = [
    #Check that this program works on a normal date
    ("January 2, 2000", datetime.datetime(2000, 1, 2, 0, 0)),
    #Check that it works with a different day form
    ("January 02 2000", datetime.datetime(2000, 1, 2, 0, 0)),
    #Check that it works with a different month form
    ("Jan 02, 2000", datetime.datetime(2000, 1, 2, 0, 0))
]

@pytest.mark.parametrize("list_1_initial, list_2_initial, list_1_final, \
                          list_2_final", remove_rows_containing_nan_cases)
def test_remove_rows_cotaining_nan_cases(list_1_initial, list_2_initial, \
                                         list_1_final, list_2_final):
    """
    """
    assert remove_rows_containing_nan(list_1_initial, list_2_initial) == \
        (list_1_final, list_2_final)

@pytest.mark.parametrize("date_string, date_time", \
                          convert_date_to_datetime_cases)
def test_convert_date_to_datetime(date_string, date_time):
    """
    """
    assert convert_date_to_datetime(date_string) == date_time