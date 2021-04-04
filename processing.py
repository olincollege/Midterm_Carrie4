"""
Establishes a set of functions needed to process data into more helpful formats.
"""
import pandas as pd
import numpy as np
import datetime as dt

def extract_directors_and_title_count(data_frame):
    """
    Takes in the dataframe of Netflix data and returns a dictionary that
    contains all of the unique directors as keys with the number of titles
    they directed as keys.

    Args:
        data_frame: an object of class pandas.core.frame.DataFrame that
                    holds a list of Netflix titles and associated properties
    
    Returns:
        director_list: a list of all directors in the input dataframe
        director_counts: a corresponding list that includes the number of
                         titles each director has directed
    """
    directors = {}

    for director in data_frame['director']:
        if ',' in director:
            for person in str(director).split(', '):
                if person not in directors:
                    directors[person] = 1
                else:
                    directors[person] += 1
        else:
            if director not in directors:
                directors[director] = 1
            else:
                directors[director] += 1
    
    director_list = list(directors.keys())
    director_counts = list(directors.values())
    return director_list, director_counts

def extract_rating_and_title_count(data_frame):
    """
    Takes in the dataframe of Netflix data and returns a dictionary that
    contains all of the unique MPAA ratings as keys with the number of titles
    with those ratings as values.

    Args:
        data_frame: an object of class pandas.core.frame.DataFrame that
                    holds a list of Netflix titles and associated properties
    
    Returns:
        rating_list: a list of all MPAA ratings in the input dataframe
        rating_counts: a corresponding list that includes the number of
                         titles with each rating
    """

    ratings = {}

    for rating in data_frame['rating']:
        if rating not in ratings:
            ratings[rating] = 1
        else:
            ratings[rating] = ratings[rating] + 1
    
    rating_list = list(ratings.keys())
    rating_counts = list(ratings.values())

    return rating_list, rating_counts

def convert_date_to_datetime(date):
    """
    Converts a string to a datetime object to help with organization
    and classification when graphing.

    Args:
        date: a string that contains a date in the form Month D, YYYY
    """

    no_comma_date = date.replace(",", "")

    date = dt.datetime.strptime(no_comma_date, "%B %d %Y")

    return date

def release_year_to_add_date(exact_date, release_year):
    """
    Finds the difference in years of an exact date and a year

    Args:
        exact_date: a datetime.datetime object that contains an exact date
        year: an integer representing a year
    
    Returns:
        an integer representing the time elapsed in years between inputs
    """
    difference = int(int(exact_date.year) - int(release_year))

    return difference

def remove_rows_containing_nan(list_1, list_2):
    """
    Removes empty values in one list and the corresponding values in a second
    list.

    Goes through each list looking for empty values, deleting them and their
    corresponding values at the same time. If the lists are of different
    lengths, the extra values will be truncated.

    Args:
        list_1: a list of values
        list_2: a second corresponding list
    
    Returns:
        list_1: a list of values with no empty values
        list_2: a second corresponding list with no empty values
    """

    combined_list = zip(list_1, list_2)

    final_list= []

    for row in list(combined_list):
        if all(row) and "NONE" not in row:
            final_list.append(row)

    resulting_lists = [[i for i, j in final_list], [j for i, j in final_list]]

    list_1 = resulting_lists[0]
    list_2 = resulting_lists[1]

    return list_1, list_2

def remove_none_entries_one_dataframe_column(data_frame_column):
    """
    Removes empty values from a column of a dataframe

    Args:
        data_frame_column: a column from a pandas dataframe
    
    Returns:
        A list containing the non-none values of the input column
    """
    list_ = list(data_frame_column)
    new_list = []

    for entry in list_:
        if entry != "NONE":
            new_list.append(entry)
    
    return new_list

def sort_list_based_on_other(list_to_order, list_to_order_by, \
                             greatest_to_least=False):
    """
    Sorts two lists in parallel, giving priority to one list for sorting.

    Orders the lists least to greatest or greatest to least based on
    user input. 

    Args:
        list_to_order: a list representing the priority list to sort by
        secondary_list: a list to be sorted in parallel with list_to_order
        greatest_to_least: A boolean representing whether to sort high to low

    Returns:
        new_list_1: the now-sorted priority list
        new_secondary_list: the now-sorted parallel list
    """
    zipped = zip(list_to_order_by, list_to_order)
    sorted_zip = sorted(zipped, reverse=greatest_to_least)

    new_tuples = zip(*sorted_zip)

    (new_list_to_order_by, new_list_to_order) = [list(new_tuple) for \
        new_tuple in new_tuples]
    
    return new_list_to_order, new_list_to_order_by

def find_year_difference(dates, years):
    """
    """
    dates = list(dates)
    years = list(years)

    (dates, years) = remove_rows_containing_nan(dates, years)

    new_dates = []

    for date in dates:
        working_date = date
        if date[0] == " ":
            working_date = working_date[1:]
        new_dates.append(working_date)

    all_dates = [convert_date_to_datetime(date) for date in new_dates]

    differences = [release_year_to_add_date(all_dates[i], years[i]) for \
        i in range(len(years))]
    
    return differences