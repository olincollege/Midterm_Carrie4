"""
Establishes a set of functions needed to process data into more helpful formats.
"""
import datetime as dt
import pandas as pd
import plots

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

    # Creates a dictionary with all of the unique director names as keys
    # and the number of titles they directed as values
    for director in data_frame["director"]:
        if "," in director:
            for person in str(director).split(", "):
                if person not in directors:
                    directors[person] = 1
                else:
                    directors[person] += 1
        else:
            if director not in directors:
                directors[director] = 1
            else:
                directors[director] += 1

    # Turns the dictionary into lists
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

    # Creates a dictionary including the unique content ratings as keys
    # and the number of titles with those ratings as values
    for rating in data_frame["rating"]:
        if rating not in ratings:
            ratings[rating] = 1
        else:
            ratings[rating] = ratings[rating] + 1

    rating_list = list(ratings.keys())
    rating_counts = list(ratings.values())

    # Takes titles rated a mystery rating "2863" and adds them to the
    # Unrated rating key
    rating_counts[rating_list.index("UR")] += \
        rating_counts[rating_list.index("2863")]

    rating_counts.pop(rating_list.index("2863"))
    rating_list.pop(rating_list.index("2863"))

    return rating_list, rating_counts

def convert_date_to_datetime(date):
    """
    Converts a string to a datetime object to help with organization
    and classification when graphing.

    Args:
        date: a string that contains a date in the form Month D, YYYY
    """

    no_comma_date = date.replace(",", "")

    # Converts the date into a datetime instance
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

    # Adds defined values to final_list. Does not include NaN or "NONE" values
    for row in list(combined_list):
        if all(row) and "NONE" not in row and row[0]==row[0] and \
                    row[1]==row[1]:
            final_list.append(row)

    # Separates the zipped file into two lists
    resulting_lists = [[first for first, second in final_list], \
        [second for first, second in final_list]]

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

    # Removes items containing "NONE" or NaN values
    for entry in list_:
        entry_comparator = entry
        if entry != "NONE" and entry_comparator == entry:
            new_list.append(entry)

    return new_list

def remove_none_entries_one_list(list_):
    """
    Removes empty values from a list

    Args:
        list_: a list of values

    Returns:
        A list containing the non-none values of the input list
    """
    new_list = []

    # Removes "NONE" or NaN values
    for entry in list_:
        entry_comparator = entry
        if entry != "NONE" and entry_comparator == entry:
            new_list.append(entry)

    return new_list

def sort_list_based_on_other(list_to_order, secondary_list, \
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

    # Combines lists to sort in parallel
    zipped = zip(list_to_order, secondary_list)
    sorted_zip = sorted(zipped, reverse=greatest_to_least)

    new_tuples = zip(*sorted_zip)

    # Separates zipped file back into two lists
    (new_list_to_order, new_secondary_list) = [list(new_tuple) for \
        new_tuple in new_tuples]

    return new_list_to_order, new_secondary_list

def find_year_difference(dates, years):
    """
    Finds the difference between a date and associated years

    Args:
        dates: A dataframe column or list containing strings that represent
               dates. They are of the form "Month DD, YYYY"
        years: A dataframe column or list containing integers that represent
               years. They are of the form YYYY.

    Returns:
        A list that contains the differences between all dates and the matching
        years. If either input contained empty or extra values, the returned
        list will not contain those rows.
    """
    dates = list(dates)
    years = list(years)

    (dates, years) = remove_rows_containing_nan(dates, years)

    new_dates = []

    # Creates a list of all of the dates and removes leading spaces
    for date in dates:
        working_date = date
        if date[0] == " ":
            working_date = working_date[1:]
        new_dates.append(working_date)

    all_dates = [convert_date_to_datetime(date) for date in new_dates]

    # Finds all of the differences and saves to list
    differences = [release_year_to_add_date(all_dates[i], years[i]) for \
        i in range(len(years))]

    return differences

def find_cases_and_pull_from_other_column(data_frame, column_1, quality, \
    column_2):
    """
    Finds all of the elements of a dataframe column that match a certain
    condition, then find the values in another column that map to those
    entries.

    Args:
        data_frame: a data frame with at least two columns to search within
        column_1: The heading of the first datafram column to check
        quality: The condition to search for within column_1
        column_2: The heading of the column from which to pull entries at the
                  indices in the first column that match the quality

    Returns:
        A list containing the items in the second column that map to the
        entries in the first column that match the inputted condition.
    """
    commonality_list = []

    # Creates a list of values in the second column with the same index as
    # values in the first column that match a specific quality
    for index, item in enumerate(data_frame[column_1]):
        if item == quality:
            commonality_list.append(data_frame[column_2][index])

    return commonality_list

def two_columns_to_violin_dataframe(data_frame, column_1, \
    column_1_legend_name, column_2, column_2_legend_name \
    ):
    """
    Using two columns of a dataframe, generates a new dataframe for
    creating of a violin plot.

    Args:
        data_frame: a large data frame with many columns
        column_1: The string heading of the first column for violin plotting
        column_1_legend_name: A string that represents how the first dataframe
                              column should be labeled in the violin plot
        column_2: The string heading of the second column for violin plotting
        column_2_legend_name: A string that represents how the second dataframe
                              column should be labeled in the violin plot

    Returns:
        A dataframe of three columns: The first column being the two input
        columns concatenated, the second being a logical list that signifies
        which side of the violin split each datapoint should be plotted to,
        and the third representing the x-axis label of the plot
    """
    list_1 = list(data_frame[column_1])
    list_2 = list(data_frame[column_2])

    (list_1, list_2) = remove_rows_containing_nan(list_1, list_2)

    # Creates a logical list that says which dataset each value belongs to
    logical = [column_1_legend_name]*len(list_1)

    logical.extend([column_2_legend_name]*len(list_2))

    list_1.extend(list_2)

    x_labels = ["All Titles"] * len(list_1)

    # Creates a dictionary to aid with creation of a pandas dataframe
    dictionary = {"PlotData":list_1, "Reviewer":logical, \
        "x_label": x_labels}

    return pd.DataFrame(dictionary)

def critics_vs_audience_scores(data_frame):
    """
    From a given dataframe, pulls out select columns and plots them
    using a violin plot

    Args:
        data_frame: A dataframe with at least two columns
    """

    data = two_columns_to_violin_dataframe(data_frame, \
        "rottentomatoes_tomatometer_score", "Critic", \
        "rottentomatoes_audience_score", "Audience")

    plots.violin_plot(["PlotData","x_label","Reviewer"],[" ", \
        "Tomatometer Score", "Critic and Audience Ratings of Netflix Titles"],\
             data)

def release_to_added_times(data_frame):
    """
    Finds the difference in years between the release years of content and the
    date the content was added to the platform

    Args:
        data_frame: a pandas dataframe that includes a Netflix catalog

    Returns:
        A list of the unique differences in years between release year and add
            date
        A list that includes the frequency of each of the values in the first
            list
    """

    differences = find_year_difference(data_frame["date_added"], \
        data_frame["release_year"])

    # Creates a dictionary that includes all of the differences and their
    # frequencies
    difference_dict = {}
    for difference in differences:
        if difference not in difference_dict:
            difference_dict[difference] = 1
        else:
            difference_dict[difference] += 1

    differences = list(difference_dict.keys())

    difference_counts = list(difference_dict.values())

    # Sorts the two lists
    (difference_counts, differences) = \
        sort_list_based_on_other(difference_counts, differences)

    return (difference_counts, differences)

def age_of_titles(data_frame):
    """
    Determines how old Netflix offerings are

    Args:
        data_frame: a pandas dataframe including the platform's offerings

    Returns:
        A list of the unique ages in years of all titles in the dataframe
        A list of frequencies of each of those values
    """

    # List of the current year
    now_list = [2021]*len(data_frame["release_year"])

    differences = []

    zipped = zip(now_list, list(data_frame["release_year"]))

    for list_1, list_2 in zipped:
        differences.append(list_1-list_2)

    # Creates a dictionary that inclues all of the differences and their
    # frequencies
    difference_dict = {}
    for difference in differences:
        if difference not in difference_dict:
            difference_dict[difference] = 1
        else:
            difference_dict[difference] += 1

    differences = list(difference_dict.keys())

    difference_counts = list(difference_dict.values())

    # Sorts the lists
    (difference_counts, differences) = \
        sort_list_based_on_other(difference_counts, differences)

    return difference_counts, differences
