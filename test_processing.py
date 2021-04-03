"""
Test functions to process the contents of a Netflix titles dataframe
"""

from collections import Counter
import pytest

from processing import (
    remove_rows_containing_nan
)

remove_rows_containing_nan_cases = [
    #Check that this program works on two short lists
    ([1, None ,3], ["a", "b", None], [1], ["a"]),
    #Check that this works on lists of different lengths
    ([1, 2, 3, 4, 5], ["a", "b"], [1, 2], ["a","b"])
]

@pytest.mark.parametrize("list_1_initial, list_2_initial, list_1_final, \
                          list_2_final", remove_rows_containing_nan_cases)
def test_remove_rows_cotaining_nan_cases(list_1_initial, list_2_initial, \
                                         list_1_final, list_2_final):
    """
    """
    assert remove_rows_containing_nan(list_1_initial, list_2_initial) == \
        (list_1_final, list_2_final)