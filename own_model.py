import numpy as np
from scipy.integrate import odeint

from probablistic_modeling import ProbableEvent, ProbableCapacity
from plotting import TwoDimFigure
from plotting import plt


class MongooseModel(object):

    _PLOT_LABELS = ("Modeled population size",)
    _FIGURE_LABELS = "year", "individuals"

    def __init__(self, r=4.27481802e-01, k=9.14540395e+03, h=8.59748557e-02):
        self.__r = r  # the intrinsic rate
        self.__k = k  # the carrying capacity
        self.__h = h  # the harvest
        _intrinsic_event = ProbableEvent(self.__r)
        _capacity = ProbableCapacity(self.__k)

        def _ode_mongoose(individual):
            return _intrinsic_event.occurs(individual) * (1 - _capacity.occurs(individual)) - self.__h * individual

        self.__odes = (_ode_mongoose,)
        self.__time_grid = None
        self.__solution = None


    @property
    def r(self):
        """the intrinsic rate"""
        return self.__r

    @property
    def k(self):
        """the carrying capacity"""
        return self.__k

    @property
    def h(self):
        """the harvest"""
        return self.__h

    @property
    def solution(self):
        return self.__solution

    @staticmethod
    def _ode_sys(fs):
        return lambda y, t: [f(*y) for f in fs]

    def apply(self, t):
        sol = odeint(MongooseModel._ode_sys(self.__odes), (30,), np.array([1979, t]))
        mongoose = sol[:, 0]
        return mongoose[1]

    def solve(self, init_vector, time_grid):
        self.__solution = odeint(MongooseModel._ode_sys(self.__odes), init_vector, time_grid)
        self.__time_grid = time_grid
        return self.__solution

    def create_figure(self, title, color=None):
        mongoose = self.__solution[:, 0]
        solution_plots = {
            MongooseModel._PLOT_LABELS[0]: (self.__time_grid, mongoose)
        }
        return TwoDimFigure(title, solution_plots, MongooseModel._FIGURE_LABELS, color)

    @staticmethod
    def draw_figure():
        plt.show()


class MongooseModel2(object):

    _PLOT_LABELS = ("Modeled population size",)
    _FIGURE_LABELS = "year", "individuals"

    def __init__(self, r=4.27481802e-01, k=9.14540395e+03, h=8.59748557e-02):
        self.__r = r  # the intrinsic rate
        self.__k = k  # the carrying capacity
        self.__h = h  # the harvest
        _intrinsic_event = ProbableEvent(self.__r)
        _capacity = ProbableCapacity(self.__k)

        def _ode_mongoose(individual):
            return _intrinsic_event.occurs(individual) * (1 - _capacity.occurs(individual)) - self.__h

        self.__odes = (_ode_mongoose,)
        # self.__equilibrium = ((0., 0.), (c / (recomm_by_drugs_indices * b), a / b))
        # ode_prey_deriv_by_prey = lambda prey, predator: a - b * predator
        # ode_prey_deriv_by_predator = lambda prey, predator: -b * prey
        # ode_predator_deriv_by_prey = lambda prey, predator: recomm_by_drugs_indices * b * predator
        # ode_predator_deriv_by_predator = lambda prey, predator: -c + recomm_by_drugs_indices * b * prey
        # self.__second_derivatives = ((ode_prey_deriv_by_prey, ode_prey_deriv_by_predator),
        #                       (ode_predator_deriv_by_prey, ode_predator_deriv_by_predator))

        # self.__jacobians = (self.__jacobian(self.__equilibrium[0]), self.__jacobian(self.__equilibrium[1]))
        self.__time_grid = None
        self.__solution = None

    # def __jacobian(self, zero_point):
    #     res = []
    #     for row in self.__second_derivatives:
    #         res_row = []
    #         for deriv in row:
    #             res_row.append(deriv(*zero_point))
    #         res.append(res_row)
    #     return res

    @property
    def r(self):
        """the intrinsic rate"""
        return self.__r

    @property
    def k(self):
        """the carrying capacity"""
        return self.__k

    @property
    def h(self):
        """the harvest"""
        return self.__h

    # @property
    # def equilibrium(self):
    #     return self.__equilibrium
    #
    # @property
    # def jacobians(self):
    #     return self.__jacobians

    @property
    def solution(self):
        return self.__solution

    @staticmethod
    def _ode_sys(fs):
        return lambda y, t: [f(*y) for f in fs]

    def apply(self, t):
        sol = odeint(MongooseModel._ode_sys(self.__odes), (30,), np.array([1979, t]))
        mongoose = sol[:, 0]
        return mongoose[1]

    def solve(self, init_vector, time_grid):
        self.__solution = odeint(MongooseModel._ode_sys(self.__odes), init_vector, time_grid)
        self.__time_grid = time_grid
        return self.__solution

    def create_figure(self, title):
        mongoose = self.__solution[:, 0]
        solution_plots = {
            MongooseModel._PLOT_LABELS[0]: (self.__time_grid, mongoose)
        }
        return TwoDimFigure(title, solution_plots, MongooseModel._FIGURE_LABELS)

    @staticmethod
    def draw_figure():
        plt.show()