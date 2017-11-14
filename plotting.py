import itertools
from matplotlib import pyplot

plt = pyplot

_FIGURE_SIZE_KEY = "figure.figsize"
# http://matplotlib.org/users/customizing.html
colors = itertools.cycle(["r", "b", "g"])

plt.rcParams[_FIGURE_SIZE_KEY] = 10, 8  # in inches


class TwoDimFigure(object):
    def __init__(self, title, plots, labels, color=None):
        # plt.figure()
        for k, v in plots.items():
            plot_type = None
            if len(v) > 2:
                plot_type = v[2]
            if plot_type == "scatter":
                plt.scatter(v[0], v[1], label=k, color=next(colors))
            else:
                if color:
                    plt.plot(v[0], v[1], label=k, color=color)
                else:
                    plt.plot(v[0], v[1], label=k, color=next(colors))
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.title(title)
        # http://matplotlib.org/users/legend_guide.html#legend-location
        plt.legend(loc=0)
