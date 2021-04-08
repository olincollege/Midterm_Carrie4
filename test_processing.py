"""
Tests data processing functions
"""
from collections import Counter
import datetime
import pytest

from processing import (
    remove_rows_containing_nan,
    convert_date_to_datetime,
)

remove_rows_containing_nan_cases = [
    #Check that this program works on two short lists
    ([1, None ,3], ["a", "b", None], [1], ["a"]),
    #Check that this works on lists of different lengths
    ([1, 2, 3, 4, 5], ["a", "b"], [1, 2], ["a","b"]),
    #Check that it works with an empty list
    ([], ["a", "b", "c"], [], [])
]

convert_date_to_datetime_cases = [
    #Check that this program works on a normal date
    ("January 2, 2000", datetime.datetime(2000, 1, 2, 0, 0)),
    #Check that it works with a different day form
    ("January 02 2000", datetime.datetime(2000, 1, 2, 0, 0)),
]

@pytest.mark.parametrize("list_1_initial, list_2_initial, list_1_final, \
                          list_2_final", remove_rows_containing_nan_cases)
def test_remove_rows_cotaining_nan_cases(list_1_initial, list_2_initial, \
                                         list_1_final, list_2_final):
    """
    Test that nan or "NONE" are removed from the input lists.

    Check that two input lists are parsed and have the incorrect values
    (nan or "NONE") removed. Should the two lists be of different lengths,
    also checks that they are both the same length.

    Args:
        list_1_initial: First input list of items
        list_2_initial: Second input list of items
        list_1_final: List containing only defined values from list_1_initial.
                      Items that mapped to undefined values in list_2_iniial
                      should also have been removed
        list_2_final: List containing only defined values from list_2_initial.
                      Items that mapped to undefined values in list_1_iniial
                      should also have been removed

    """
    assert remove_rows_containing_nan(list_1_initial, list_2_initial) == \
        (list_1_final, list_2_final)

@pytest.mark.parametrize("date_string, date_time", \
                          convert_date_to_datetime_cases)
def test_convert_date_to_datetime(date_string, date_time):
    """
    Test that string-form dates are properly converted into datetime objects

    Checks that string dates are correctly converted into instances of the 
    datetime class.

    Args:
        date_string: A string that represents a date of the form
                     "Month DD, YYYY" or "Month D, YYYY" (if applicable)
        date_time: The correct datetime instance that matches the string date
    """
    assert convert_date_to_datetime(date_string) == date_time
