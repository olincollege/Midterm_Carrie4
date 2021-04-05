"""
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def bubble_graph(x_axis=None, y_axis=None, labels=None, graph_title=None, \
                 x_axis_title=None, y_axis_title=None,index=-1):
    """
    Creates a bubble graph on an x and y plot where 
    the size of each bubble represents more data :)

    Arguments:
    x_axis: list of integers or strings to plot on the x_axis
    y_axis: listof integers to plot on the y_axis
    labels: a list of strings that represent pie chart labels
    graph_title: title of graph in string form
    x_axis: x_axis label of graph in string form
    y_axis: y_axis label of graph in string form

    Returns: none, displays graph 

    """

    #Defines the color of the bubbles
    colors = np.random.rand(len(x_axis[0:index]))

    #Defines what goes on th X-Axis in an int form
    u, ind = np.unique(x_axis[0:index], return_inverse=True)

    #Equation for size of each dot
    size = [element * 100
    for element in y_axis[0:index]]

    # Create scatterplot. alpha controls the opacity and s controls the size.
    ax = sns.scatterplot(x=ind, y=y_axis[0:index], alpha = 0.5,s = size, \
        hue = colors)

    #Set Axis limits
    ax.set_xlim(0,6)
    ax.set_ylim(0, 5)

    #For each point, we add a text inside the bubble
    for line in range(0,ind[0]):
        ax.text(ind[line], y_axis[line], labels[line], \
            horizontalalignment='center', size=10, color='black', \
                weight='semibold')
    plt.xticks(range(len(u)), u)

    #Label graph
    plt.xlabel("Release Year", size=16)
    plt.ylabel("Number of Directed movies", size=16)
    plt.title("Directed movies vs Release Year", size = 16)

    plt.show()

    return None

def bar_graph(x_data=["1"], y_data=[1],x_label="",\
    y_label="",graph_title="",color = "red"):


    plt.style.use("ggplot")
    plt.bar(x_data,y_data, color = color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title)
    plt.show()
       
    return None

def pie_chart(labels, sizes,end_index,start_index = 0):
    """
    Creates a pie chart from a list of integers where each slice is
    represented by the integer divided by the sum of the list of integers

    Arugments:
    labels: A list of strings representing a label for each slice of the chart
    sizes: A list of integers associated with each label
    end_index: an intiger representing the end range of data to plot 
                (exclusive)
    start_index: An itneger representign the start range of data to plot
                (inclusive)

    Return: None, plots a pi chart
    """
    
    label = labels[start_index:end_index]
    
        
    sizes = [size/sum(sizes[start_index:end_index]) for size in \
        sizes[start_index:end_index]]

    for count, chunk in enumerate(sizes):
        if chunk < .02:
            label[count] = ""

    explode_index =sizes.index(max(sizes))
    explode = [0] * (len(label))
    explode[explode_index] = .11

    fig1, ax1 = plt.subplots()
    
    def my_autopct(pct):
        return ('%1.1f%%' % pct) if pct > 4 else ''

    ax1.pie(sizes, explode=explode, labels=label, autopct=my_autopct, \
        shadow=False, startangle=90, normalize = False)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')  

    plt.legend(labels[start_index:end_index], loc="center left")
    
    plt.show()

    return None



def violin_plot(y_label,data,conditional, legend_label = "" ,x_label = None,x_title="Set X axis",y_title="", \
    graph_title="Set title", splitLogic = True):
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
    plt.clf()
    sns.set_theme(style="whitegrid")
    ax = sns.violinplot(x = x_label,y = y_label, hue= conditional,data = data, orient = "v", cut = 0, split=splitLogic, palette="rocket")
    ax.set(xlabel='')
    plt.show()

    return None

def color_changer(color_list = []):
    
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
    return None

def plot_format():
    sns.set(font='Franklin Gothic Book',
        rc={
    'axes.axisbelow': False,
    'axes.edgecolor': 'lightgrey',
    'axes.facecolor': 'None',
    'axes.grid': False,
    'axes.labelcolor': 'dimgrey',
    'axes.spines.right': False,
    'axes.spines.top': False,
    'figure.facecolor': 'white',
    'lines.solid_capstyle': 'round',
    'patch.edgecolor': 'w',
    'patch.force_edgecolor': True,
    'text.color': 'dimgrey',
    'xtick.bottom': False,
    'xtick.color': 'dimgrey',
    'xtick.direction': 'out',
    'xtick.top': False,
    'ytick.color': 'dimgrey',
    'ytick.direction': 'out',
    'ytick.left': False,
    'ytick.right': False})
    sns.set_context("notebook", rc={"font.size":16,
                                    "axes.titlesize":20,
                                    "axes.labelsize":18})
    return None
######################################################