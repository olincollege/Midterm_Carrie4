# The Net Netflix Casts

## Overview

Our project seeks to examine Netflix's offerings and look for trends within its catalogue. The code included in this project is designed to facilitate the processing and interpreting of its offerings. Netflix, Flixable, and Rotten Tomatoes are not affiliated with this project in any way.

## Retrieving Data

In order to retrieve the .csv files included in this repository, the user needs an API authentication key for the Kaggle website. To obtain this key, create an account at [Kaggle.com](https://www.kaggle.com). After doing this, navigate into the account settings and scroll down to a section labeled API. Click the button `Create New API Token` and save the token to the user's computer. 

Once that file has been saved, the python file `data_retrieval.py` should run properly and save the .csv files `netflix_titles.csv` and `netflix_titles_enriched.csv` to the local directory. These files as well as the libraries `pandas`, `seaborn`, `numpy`, and `datetime` are all that are needed to execute the rest of the code. 

Explanations of the processes taken to scrape data from [Flixable](https://www.kaggle.com/shivamb/netflix-shows) and [Rotten Tomatoes](https://www.kaggle.com/eugenioscionti/scraping-rotten-tomatoes-to-enrich-netflix-dataset) are available at the hyperlinks. 

## Developing Plots

The code in `NetflixTrends.ipynb` explains how the data was processed before it was compiled into graphs. There is further explanation within the function- and file-level docstrings that should provide sufficient scaffolding to be able to execute the code on other elements of the dataframe, or of elements of different dataframes. 

Make sure to run the first code cell in the Methodology section of `NetflixTrends.ipynb` to assure that the correct variables are set. Proceed by running all of the other cells in order, and the code should run without error.

With commented, functional code for all of the different steps taken to turn the .csv file into plots, the rest of the process should be relatively straightforward.

## Testing the Code

Running tests on the code is relatively simple. By opening the file `test_processing.py` the behavior of the processing functions is affirmed. If the processing code is changed, more tests can be added and the testing code updated to adapt to those changes.