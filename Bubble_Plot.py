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



del directors['NONE']
all_release_years = list(release_years.keys())
all_durations = list(durations.keys())
all_directors = list(directors.keys())
director_title_count = list(directors.values())
all_actors = list(cast.keys())
actor_title_count = list(cast.values())
all_ratings = list(ratings.keys())
ratings_title_count = list(ratings.values())


def bubble_graph(x_axis=None, y_axis=None, extra_axis=None, graph_title=None, x_axis_title=None, y_axis_title=None,index=None):
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

def pie_chart(labels, sizes,end_index,start_index = 0):
   
    labels = labels[start_index:end_index]

    sizes = [size/sum(sizes[start_index:end_index]) for size in sizes[start_index:end_index]]

    explode_index =sizes.index(max(sizes))
    explode = [0] * (len(labels))
    explode[explode_index] = .11

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    #centre_circle = plt.Circle((0,0),0.70,fc='white')
    #fig = plt.gcf()
    #fig.gca().add_artist(centre_circle)

    plt.show()
def violin_plot(x_data=None,y_axis=None,x_title=None,Y_title=None,graph_title=None):

    axs[1, 4].violinplot(data[-1:], pos[-1:], points=200, vert=False, widths=1.1,
        showmeans=True, showextrema=True, showmedians=True,
        quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
    axs[1, 4].set_title('Custom violinplot 10', fontsize=fs)


    for ax in axs.flat:
        ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()

#pie_chart(all_ratings, ratings_title_count,-1, 0)
#bubble_graph()
violin_plot([1,2,2,3,3,3,4,4,5],[1,2,3,2,1])
