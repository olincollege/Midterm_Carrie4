import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
netflix_data = pd.read_csv('netflix_titles.csv')
df = pd.DataFrame(netflix_data)
df.fillna("NONE", inplace = True)

directors = {}
cast = {}
ratings = {}
country = {}
durations = {}
release_years = {}

for director in netflix_data['director']:
    if director not in directors:
        directors[director] = 1
    else:
        directors[director] += 1

for index, value in enumerate(netflix_data['cast']):
    for member in list(str(value).split(", ")):
        if member not in cast:
            cast[member] = 1
        else:
            cast[member] +=1

for rating in netflix_data['rating']:
    if rating not in ratings:
        ratings[rating] = 1
    else:
        ratings[rating] = ratings[rating] + 1

# Creates dictionary for how many times a show is a particular length
for duration in netflix_data['duration']:
    if duration not in durations:
        durations[duration] = 1
    else:
        durations[duration] = durations[duration] + 1   

for year in netflix_data['release_year']:
    if year not in release_years:
        release_years[year] = 1
    else:
        release_years[year] = release_years[year] + 1


print(release_years)
del directors['NONE']
all_release_years = list(release_years.keys())
release_years_count = list(release_years.values())
all_durations = list(durations.keys())
all_directors = list(directors.keys())
director_title_count = list(directors.values())
all_actors = list(cast.keys())
actor_title_count = list(cast.values())
all_ratings = list(ratings.keys())
ratings_title_count = list(ratings.values())


def bubble_graph(x_axis=None, y_axis=None, graph_title=None, x_axis_title=None, y_axis_title=None,index=None):
    """
    Creates a bubble graph on an x and y plot where 
    the size of each bubble represents more data :)

    Arguments:
    x_axis: list of integers or strings to plot on the x_axis
    y_axis: listof integers to plot on the y_axis
    graph_title: title of graph in string form
    x_axis: x_axis label of graph in string form
    y_axis: y_axis label of graph in string form

    Returns: none, displays graph 

    """
    
    index = 13
    #Defines the color of the bubbles
    colors = np.random.rand(len(all_release_years[0:index]))

    #Defines what goes on th X-Axis in an int form
    u, ind = np.unique(all_release_years[0:index], return_inverse=True)

    #Equation for size of each dot
    size = [element * 100
    for element in director_title_count[0:index]]

    # Create scatterplot. alpha controls the opacity and s controls the size.
    ax = sns.scatterplot(ind, director_title_count[0:index], alpha = 0.5,s = size)

    #Set Axis limits
    ax.set_xlim(0,6)
    ax.set_ylim(0, 5)

    #For each point, we add a text inside the bubble
    for line in range(0,ind[0]):
        ax.text(ind[line], director_title_count[line], all_directors[line], horizontalalignment='center', size=10, color='black', weight='semibold')
    plt.xticks(range(len(u)), u)

    #Label graph
    plt.xlabel("Release Year", size=16)
    plt.ylabel("Number of Directed movies", size=16)
    plt.title("Directed movies vs Release Year", size = 16)

    plt.show()

    return None

def pie_chart(labels, sizes,end_index,start_index = 0):
    """
    Creates a pie chart from a list of integers where each slice is
    represented by the integer divided by the sum of the list of integers

    Arugments:
    labels: A list of strings representing a label for each slice of the chart
    sizes: A list of integers associated with each label
    end_index: an intiger representing the end range of data to plot (exclusive)
    start_index: An itneger representign the start range of data to plot(inclusive)

    Return: None, plots a pi chart
    """
    labels = labels[start_index:end_index]

    sizes = [size/sum(sizes[start_index:end_index]) for size in sizes[start_index:end_index]]

    explode_index =sizes.index(max(sizes))
    explode = [0] * (len(labels))
    explode[explode_index] = .11

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

    return None
def violin_plot(x_data,x_title="Set X axis",y_title="",graph_title="Set title"):
    """
    Takes a list of integer and creates a violin plot

    Arguments: 
    x_data: List of integers, or floats to be plotted based
    on frequency each integer occurs
    x_title: A string representing the x-axis label
    y_title: A string representing the y-axis title
    title: A strign representing the title of the graph

    Returns: None, displays a graph
    """

    fs = 10  # fontsize
    pos = [0]
 
    fig, ax = plt.subplots(1, 1, figsize = (8,8))
    
    violin_parts = ax.violinplot(x_data, pos, points=200, vert=True, widths=1.1,
                        showmeans=False, showextrema=False, showmedians=False,
                        quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
    
    for pc in violin_parts['bodies']:
        pc.set_facecolor("Blue")
        pc.set_linewidth(2)
        pc.set_edgecolor('black')
        pc.set_alpha(.5)

    plt.suptitle(f"{graph_title}")
    plt.xlabel(f"{x_title}")
    plt.ylabel(f"{y_title}")
    plt.subplots_adjust(hspace=0.4)
    plt.show()

    return None
#########################################################################
pie_chart(all_ratings, ratings_title_count,-1, 0)
#bubble_graph()
year_list = []
for year in netflix_data['release_year']:
    year_list.append(year)
violin_plot(year_list,"Hello","world","Star" )
