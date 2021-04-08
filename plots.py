"""
Handles all plotting functionalities including plotting data as well as,
formatting plots.
"""
import matplotlib.pyplot as plt
import seaborn as sns



def bar_graph(titles,x_data=1, y_data=1,color = "red"):

    """
    Uses two lists of integers or floats to create a bar graph

    Arguments:
    x_data: list of floats or integers the same length as y_data
    y_data: list of floats or integers the same length as x_data
    titles: A list of strings with 3 values, representing the x-axis label,
    y-axis label, and graph title respectively
    color: String representing colors supported by the matplotlib, changing the
           color of plotted bars

    """
    x_label = titles[1]
    y_label = titles[2]
    graph_title = titles[3]

    plt.style.use("ggplot")
    plt.bar(x_data,y_data, color = color)
    plt.xlabel(x_label, fontsize = 24)
    plt.ylabel(y_label, fontsize = 24)
    plt.title(graph_title, fontsize = 36)
    plt.show()



def pie_chart(labels, sizes,end_index,start_index = 0):
    """
    Creates a pie chart from a list of integers where each slice is
    represented by the integer divided by the sum of the list of integers

    Arugments:
    labels: A list of strings representing a label for each slice of the chart
            where the label of any value less than 2% is removed to eliminate
            text clipping
    sizes: A list of integers the same length of labels, representing each labels
            value
    end_index: An int representing the end range of data to plot
               (exclusive)
    start_index: An int representing the start range of data to plot
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
    explode[explode_index] = .05
    _, ax1 = plt.subplots()

    def my_autopct(pct):
        return ('%1.1f%%' % pct) if pct > 4 else ''

    ax1.pie(sizes, explode=explode, labels=label, autopct=my_autopct, \
        shadow=False, startangle=90, normalize = False, textprops={'fontsize':24})
    ax1.axis('equal')
    plt.legend(labels[start_index:end_index], loc="center left", fontsize= 24)
    plt.show()


def violin_plot(headers,titles,data, splitlogic = True):
    """
    Plots a violin plot with the optional parameters, such as split,
    which plots two datasets on the same violin plot, or the ability
    to plot multiple violin plots with a single dataset

    Arguments:
    headers: A list of strings 3 values logn where the first string is the name
             of the data header, a column containing all data points. The
             second column is a string of the name of the plot_index, which
             dictates which plot the data belongs to, even in the case of a
             single plot. The last string is the conditional_header, named
             after the column that dictates which side of the splitted violin
             plots to plot the data on, when split = True.
    data: a pandas dataframe containing at least data in one column, and a
    second column, the plot_index. Conditional_header is optional based
    on if split is True or not.
    titles: a list of Strings where the first string represents the x-axis title,
    the second represents the axis title and the last represents the graph title


    Returns: None, displays a graph
    """
    data_header = headers[1]
    plot_index = headers[2]
    conditional_header = headers[3]

    xlabel = titles[1]
    ylabel = titles[2]
    graph_title = titles[3]
    plt.clf()
    sns.set_theme(style="whitegrid")
    sns.set(font_scale=2)
    plot_one = sns.violinplot(x = plot_index,y = data_header, hue= conditional_header,data = data,\
         orient = "v", cut = 0, split=splitlogic, palette="rocket", )
    plot_one.set(xlabel=xlabel)
    plot_one.set(ylabel=ylabel)

    plot_one.set_title(graph_title)
    plt.show()


def color_changer(color_list):
    """
    Takes a list of hexadecimal colors to set a defualt color palette for
    matplotlib to change style of graphs. Called before plotting
    a graph.

    Arguments:
    color_list: List of stings representing colors in hexadecimal,such as
    (##0077ff)
    """
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)



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
