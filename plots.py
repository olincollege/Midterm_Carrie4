"""
Handles all plotting functionalities including plotting data as well as,
formatting plots. 
"""
import pylint
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def bar_graph(x_data=["1"], y_data=[1],x_label="",\
    y_label="",graph_title="",color = "red"):
    
    """
    Uses two lists of data to create bar graphs

    Arguments: 
    x_data: list of floats or integers the same
    length as y_data
    y_data: list of floats or integers the same 
    length as x_data
    x_label: String representing the label on the
    x-axis
    y_label: String representing the label on the 
    y_axis
    graph_title: String representing title of graph
    color: String representing colors supported by the
    matplotlib, changign the color of plotted bars

    """

    plt.style.use("ggplot")
    plt.bar(x_data,y_data, color = color)
    plt.xlabel(x_label, fontsize = 24)
    plt.ylabel(y_label, fontsize = 24)
    plt.title(graph_title, fontsize = 36)
    plt.show()
       
    return None

def pie_chart(labels, sizes,end_index,start_index = 0):
    """
    Creates a pie chart from a list of integers where each slice is
    represented by the integer divided by the sum of the list of integers

    Arugments:
    labels: A list of strings representing a label for each slice of the chart
    where any value less than 2% on the chart does not have a label to eliinate
    text clipping
    sizes: A list of integers the same length of labels, representing wach labels
            value 
    end_index: An intiger representing the end range of data to plot 
            (exclusive)
    start_index: An itneger representign the start range of data to plot
            (inclusive)

    """

    label = labels[start_index:end_index]
    sizes = [size/sum(sizes[start_index:end_index]) for size in \
        sizes[start_index:end_index]]
    explode_index =sizes.index(max(sizes))

    for count, chunk in enumerate(sizes):
        if chunk < .02:
            label[count] = ""

    explode = [0] * (len(label))
    explode[explode_index] = .11
    fig1, ax1 = plt.subplots()
    
    def my_autopct(pct):
        return ('%1.1f%%' % pct) if pct > 4 else ''

    ax1.pie(sizes, explode=explode, labels=label, autopct=my_autopct, \
        shadow=False, startangle=90, normalize = False, textprops={'fontsize':24})
    ax1.axis('equal')  
    plt.legend(labels[start_index:end_index], loc="center left", fontsize= 24)
    plt.show()
    return None


def violin_plot(data_header,data,conditional_header = None,plot_index = None,x_title="Set X axis",\
        y_title="",graph_title="Set title", splitLogic = True):
    """
    Plots a violin plot with the optional parameters, such as split,
    wich plots two datasets on the same violin plot, or the ability
    to plot multiple violin plots with a single dataset  

    Arguments:
    data_header: String the same name of the header of the data column
    data: a pandas dataframe containing at least data in one column, and a 
    second column of the plot_index. Conditional_header is optional based
    on if split is True or not.
    conditional_header: A string the same name of a column header. The
    dataframe column associated must only have 2 unique values, which dictate
    which side of the violin plot the data belongs on when using split
    plot_index: A string the same name of a header in the dataframe
    representing which violin plot the data belongs to (Used to create
    multiple violin plots)
    x_title: String representing the label on thex-axis
    y_title: String representing the label on the y_axis
    graph_title: String representing title of graph
    splitLogic: Bool representing whether to plot split violin plots based
    on the conditional_header.
    

    Returns: None, displays a graph
    """
    plt.clf()
    sns.set_theme(style="whitegrid")
    sns.set(font_scale=2)
    ax = sns.violinplot(x = plot_index,y = data_header, hue= conditional_header,data = data,\
         orient = "v", cut = 0, split=splitLogic, palette="rocket", )
    ax.set(xlabel='')
    ax.set_title(graph_title)
    plt.show()

    return None


def color_changer(color_list = []):
    """
    Takes a list of Hexadecimal colors to set a defualt color palette for
    matplotlib to change style of graphs. Called before plotting
    a graph.

    Arguments: 
    color_list: List of stings representing colors in hexadecimal,such as
    (##0077ff)
    """    
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
    return None


def plot_format():
    """
    Function used to format plots with a specific style. Called before 
    plotting a graph.
    """
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