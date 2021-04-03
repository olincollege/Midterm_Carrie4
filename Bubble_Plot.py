import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_graph(graph_title, x_axis_title, y_axis_title, ,,index):

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

del directors['NONE']
all_release_years = list(release_years.keys())
all_durations = list(durations.keys())
all_directors = list(directors.keys())
director_title_count = list(directors.values())
all_actors = list(cast.keys())
actor_title_count = list(cast.values())
all_ratings = list(ratings.keys())
ratings_title_count = list(ratings.keys())


#########################################################
 

#########################################################

###Begin setting up plot
plt.clf()

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