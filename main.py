from plotting import TwoDimFigure
from plotting import plt

from own_model import MongooseModel, MongooseModel2

PLOT_LABELS = ("Exact population size", "Inexact population size", "Captures")
FIGURE_LABELS = "year", "individuals"

# chart values
KNOWN_POP_SIZE_VALUES = (30, 6141, 169)
KNOWN_POP_SIZE_VALUES_YEARS = (1979, 2000, 2011)
ROUGH_POP_SIZE_VALUES = (50, 160, 900, 2500, 5800, 5400, 4500, 700, 400)
ROUGH_POP_SIZE_VALUES_YEARS = (1980, 1983, 1990, 1993, 1999, 2001, 2003, 2009, 2010)
CAPTURE_NUM_VALUES = (0,
                      0, 0, 0, 60, 60, 60, 60, 60, 60, 60,
                      60, 60, 60, 851, 827, 1144, 1314, 1628, 1356, 2282,
                      3884, 3375, 2199, 2572, 2529, 2585, 2705, 779, 941, 601,
                      311, 150)

# milestones
RELEASE_YEAR = 1979
HOME_MADE_TRAPS = 1983
BUYBACK_SYSTEM = 1993
GOVERNMENT_ERADICATION_PROJECT = 2000
KILL_TRAPS = 2003
ADVANCED_KILL_TRAPS = 2009
LAST_RESEARCH_YEAR = 2011


YEARS = tuple(range(RELEASE_YEAR, LAST_RESEARCH_YEAR + 1))

FIRST_PART_START_YEAR, FIRST_PART_FINISH_YEAR = RELEASE_YEAR, GOVERNMENT_ERADICATION_PROJECT
FIRST_PART_YEARS = tuple(range(FIRST_PART_START_YEAR, FIRST_PART_FINISH_YEAR + 1))

SECOND_PART_START_YEAR, SECOND_PART_FINISH_YEAR = GOVERNMENT_ERADICATION_PROJECT, LAST_RESEARCH_YEAR
SECOND_PART_START_YEARS = tuple(range(SECOND_PART_START_YEAR, SECOND_PART_FINISH_YEAR + 1))


plt.figure()
initial_values_plots = {
    PLOT_LABELS[0]: (KNOWN_POP_SIZE_VALUES_YEARS, KNOWN_POP_SIZE_VALUES,
                     "scatter"),
    PLOT_LABELS[1]: (ROUGH_POP_SIZE_VALUES_YEARS, ROUGH_POP_SIZE_VALUES,
                     "scatter"),
    PLOT_LABELS[2]: (YEARS, CAPTURE_NUM_VALUES)
}
TwoDimFigure("Mongoose population dynamics", initial_values_plots,
             FIGURE_LABELS)

model = MongooseModel()

# solution
MONGOOSE0 = 30
y0 = (MONGOOSE0,)

model.solve(y0, FIRST_PART_YEARS)
model.create_figure("Mongoose population dynamics", "cyan")

model = MongooseModel(k=2.89068494e+03, h=0.64819849)
MONGOOSE0 = 6141
y0 = (MONGOOSE0,)
model.solve(y0, SECOND_PART_START_YEARS)
model.create_figure("Mongoose population dynamics", "cyan")


plt.savefig("res.png")



