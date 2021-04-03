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
        date: a string
    """

    no_comma_date = date.replace(",", "")

    date = dt.datetime.strptime(no_comma_date, "%B %d %Y")

    return date

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
        if all(row) and row[0] is not "NONE":
            final_list.append(row)

    resulting_lists = [[i for i, j in final_list], [j for i, j in final_list]]

    list_1 = resulting_lists[0]
    list_2 = resulting_lists[1]

    return list_1, list_2

def sort_list_greatest_to_least(list_to_order, counts, ordered_list=None):
    """
    """
    if not ordered_list:
        ordered_list = []
    
    if len(ordered_list) == 25:
        return ordered_list
    
    item = list_to_order[counts.index(max(counts))]

    ordered_list.append(item)

    list_to_order.remove(item)

    counts.remove(max(counts))
    
    return sort_list_greatest_to_least(list_to_order, counts, ordered_list)