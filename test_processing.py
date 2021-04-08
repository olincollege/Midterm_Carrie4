"""
Tests data processing functions
"""
import datetime
import pytest

from processing import (
    remove_rows_containing_nan,
    convert_date_to_datetime,
    release_year_to_add_date,
    remove_none_entries_one_list,
    sort_list_based_on_other
)

remove_rows_containing_nan_cases = [
    #Check that this program works on two short lists
    ([1, None ,3], ["a", "b", None], [1], ["a"]),
    #Check that this works on lists of different lengths
    ([1, 2, 3, 4, 5], ["a", "b"], [1, 2], ["a","b"]),
    #Check that it works with an empty list
    ([], ["a", "b", "c"], [], []),
    #Check that it works with NaN values
    ([float("NaN"), 1], ["a","b"], [1], ["b"])
]

convert_date_to_datetime_cases = [
    #Check that this program works on a normal date
    ("January 2, 2000", datetime.datetime(2000, 1, 2, 0, 0)),
    #Check that it works with a different day form
    ("January 02 2000", datetime.datetime(2000, 1, 2, 0, 0)),
]

release_year_to_add_date_cases = [
    #Check that this works with the intended inputs
    (datetime.datetime(2000, 1, 2), 1990, 10),
    #Check that this works for year values after the datetime object
    (datetime.datetime(2000,1,2), 2003, -3),
    #Check that it behaves correctly when the year is the same year
    (datetime.datetime(2000,1,2),2000,0),
]

remove_none_entries_one_list_cases = [
    #Check that it works with the value "NONE"
    ([0, 1, 2, "NONE"], [0, 1, 2]),
    #Check that it works with an empty value
    ([0, 1, 2, ], [0, 1, 2]),
]

sort_list_based_on_other_cases = [
    #Check that this works on basic input
    ([19,2,3,1,7],["a","b","d","c","e"],[1,2,3,7,19],["c","b","d","e","a"]),
    #Check that it works differently if the inputs are switched
    (["a","b","d","c","e"],[19,2,3,1,7],["a","b","c","d","e"],[19,2,1,3,7]),
    #Check that a sorted list does nothing
    (["a","b","c","d","e"],[19,2,1,3,7],["a","b","c","d","e"],[19,2,1,3,7]),
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


@pytest.mark.parametrize("date, year, diff", release_year_to_add_date_cases)
def test_release_year_to_add_date(date, year, diff):
    """
    Test that the difference in years between a date and a year is correctly
    calculated

    Interpret a datetime object and find the number of years between that date
    and a year value.

    Args:
        date: a datetime object representing an exact date
        year: an integer representing a year
        diff: an integer representing the number of years difference between
              "date" and "year" arguments
    """
    assert release_year_to_add_date(date, year) == diff


@pytest.mark.parametrize("bad_list, clean_list", \
                         remove_none_entries_one_list_cases)
def test_remove_none_entries_one_list_cases(bad_list, clean_list):
    """
    Test that lists containing empty values or "NONE" strings are returned
    without those invalid values.

    Args:
        bad_list: A list that may contain invalid values
        clean_list: The input "bad_list" with the invalid values removed
    """
    assert remove_none_entries_one_list(bad_list) == clean_list


@pytest.mark.parametrize("list_1, list_2, list_1_sorted, list_2_sorted", \
    sort_list_based_on_other_cases)
def test_sort_list_based_on_other(list_1,list_2,list_1_sorted,list_2_sorted):
    """
    Test that this function properly sorts two lists based on the contents of
    one list. 

    Should reorder both lists so that one of them is in the natural sorted()
    order, and the other list's values should be mapped to the same values
    in the first list pre-sorting

    Args:
        list_1: A list to sort by
        list_2: A list that maps to the values in "list_1"
        list_1_sorted: The sorted first list
        list_2_sorted: The second list, sorted based on the first list
    """
    assert sort_list_based_on_other(list_1, list_2) == (list_1_sorted, \
        list_2_sorted)
