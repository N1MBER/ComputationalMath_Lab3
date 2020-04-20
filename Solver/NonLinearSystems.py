import math
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import warnings
from Solver import NonLinearEquations

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class Qualifier:
    eq_count = 0
    types = []
    accuracy = 0
    approximation = []
    area = 0

    def __init__(self):
        self.start()

    def start(self):
        self.check_area()
        self.check_Type()
        self.set_accuracy()
        self.set_approximation()
        calculator = Calculator(self.types, self.accuracy, self.approximation)
        calculator.calculate()
        printResult(calculator)
        del calculator

    def check_area(self):
        while 1:
            try:
                print("Select type:\n"
                      "\t1. Plane with \'oX\', \'oY\'.\n"
                      "\t2. Space with \'oX\', \'oY\', \'oZ\'.\n")
                answer = int(input("Type: ").strip())
                if answer == 1:
                    self.area = 1
                    break
                elif answer == 2:
                    self.area = 2
                    break
                else:
                    NonLinearEquations.getReadyAnswer(1)
                    continue
            except TypeError:
                NonLinearEquations.getReadyAnswer(1)
                continue

    def check_Type(self):
        count = 0
        if self.area == 1:
            while 1:
                if count >= 2:
                    break
                else:
                    try:
                        print("\nPlease choose a equations:\n"
                              "\t1. 0.1x^2 + x + 0.2y^2 - 0.3 = 0\n"
                              "\t2. 0.2x^2 + y - 0.1xy - 0.7 = 0\n"
                              "\t3. x + y - x^2 - 5 = 0 \n"
                              "\t4. 3y + 2x^3 - 2 = 0 \n")
                        answer = int(input("Variant: ").strip())
                        if answer == 1:
                            self.types.append(1)
                        elif answer == 2:
                            self.types.append(2)
                        elif answer == 3:
                            self.types.append(3)
                        elif answer == 4:
                            self.types.append(4)
                        else:
                            NonLinearEquations.getReadyAnswer(1)
                            continue
                        count += 1
                    except TypeError:
                        NonLinearEquations.getReadyAnswer(1)
                        continue
        elif self.area == 2:
            while 1:
                if count >= 3:
                    break
                else:
                    try:
                        print("\nPlease choose a equations:\n"
                              "\t1. 2x^2 - y + 4z = 0\n"
                              "\t2. sin(x) - sin(y) - sin(z) = 0\n"
                              "\t3. x + y^2 / 2 - 2z = 0 \n"
                              "\t4. 2x - 4zy + 5 = 0 \n")
                        answer = int(input("Variant: ").strip())
                        if answer == 1:
                            self.types.append(1)
                        elif answer == 2:
                            self.types.append(2)
                        elif answer == 3:
                            self.types.append(3)
                        elif answer == 4:
                            self.types.append(4)
                        else:
                            NonLinearEquations.getReadyAnswer(1)
                            continue
                        count += 1
                    except TypeError:
                        NonLinearEquations.getReadyAnswer(1)
                        continue

    # def set_coefficient(self):
    #     while 1:
    #         try:
    #             print("Please write coefficient \'a\',\'b\',\'c\':\n ")
    #             list_count = list(input("Coefficient: ").strip().split(" "))
    #             print(list_count)
    #             if len(list_count) == 3:
    #                 cof = []
    #                 for i in list_count:
    #                     cof.append(float(i))
    #                 self.coefficient.append(cof)
    #                 break
    #             else:
    #                 NonLinearEquations.getReadyAnswer(1)
    #                 continue
    #         except TypeError:
    #             NonLinearEquations.getReadyAnswer(1)
    #             continue

    def set_accuracy(self):
        while 1:
            try:
                print("Please set accuracy:\n ")
                accuracy = float(input("Accuracy: ").strip())
                if accuracy > 0:
                    self.accuracy = accuracy
                    break
                else:
                    NonLinearEquations.getReadyAnswer(1)
                    continue
            except TypeError:
                NonLinearEquations.getReadyAnswer(1)
                continue

    def set_approximation(self):
        if self.area == 1:
            while 1:
                try:
                    print("Please set approximation \'x\', \'y\':\n ")
                    list_approximation = list(input("Approximation: ").strip().split(" "))
                    if len(list_approximation) == 2:
                        self.approximation.append(float(list_approximation[0].strip()))
                        self.approximation.append(float(list_approximation[1].strip()))
                        break
                    else:
                        NonLinearEquations.getReadyAnswer(1)
                        continue
                except TypeError:
                    NonLinearEquations.getReadyAnswer(1)
                    continue
        elif self.area == 2:
            while 1:
                try:
                    print("Please set approximation \'x\', \'y\', \'z\':\n ")
                    list_approximation = list(input("Approximation: ").strip().split(" "))
                    if len(list_approximation) == 3:
                        self.approximation.append(float(list_approximation[0].strip()))
                        self.approximation.append(float(list_approximation[1].strip()))
                        self.approximation.append(float(list_approximation[2].strip()))
                        break
                    else:
                        NonLinearEquations.getReadyAnswer(1)
                        continue
                except TypeError:
                    NonLinearEquations.getReadyAnswer(1)
                    continue
        else:
            NonLinearEquations.getReadyAnswer(1)


class Calculator:
    type_equations = []
    accuracy = 0
    status = 0
    x = 0
    y = 0
    z = 0
    x_previous = 0
    y_previous = 0
    z_previous = 0
    iterations = 0

    def __init__(self, types, accuracy, approximation):
        self.type_equations = types
        self.accuracy = accuracy
        self.iterations = 0
        self.status = 0
        self.x = 0
        self.y = 0
        self.x_previous = approximation[0]
        self.y_previous = approximation[1]
        if len(approximation) == 3:
            self.z = 0
            self.z_previous = approximation[2]

    def calculate(self):
        if len(self.type_equations) == 2:
            while 1 and self.iterations < 250000:
                self.x = self.x_previous - get_Determinant(
                    self.get_A(1, self.x_previous, self.y_previous, self.z_previous)) / get_Determinant(
                    self.get_jacobian(self.x_previous, self.y_previous, self.z_previous))
                self.y = self.y_previous - get_Determinant(
                    self.get_A(2, self.x_previous, self.y_previous, self.z_previous)) / get_Determinant(
                    self.get_jacobian(self.x_previous, self.y_previous, self.z_previous))
                self.iterations += 1
                if abs(self.x - self.x_previous) <= self.accuracy and abs(
                        self.y - self.y_previous) <= self.accuracy:
                    self.accuracy = abs(self.x - self.x_previous + self.y - self.y_previous) / 2
                    break
                self.x_previous = self.x
                self.y_previous = self.y
            if self.iterations == 250000:
                self.status = 1
        else:
            while 1 and self.iterations < 250000:
                self.x = self.x_previous - get_Determinant(
                    self.get_A(1, self.x_previous, self.y_previous, self.z_previous)) / get_Determinant(
                    self.get_jacobian(self.x_previous, self.y_previous, self.z_previous))
                self.y = self.y_previous - get_Determinant(
                    self.get_A(2, self.x_previous, self.y_previous, self.z_previous)) / get_Determinant(
                    self.get_jacobian(self.x_previous, self.y_previous, self.z_previous))
                self.z = self.z_previous - get_Determinant(
                    self.get_A(3, self.x_previous, self.y_previous, self.z_previous)) / get_Determinant(
                    self.get_jacobian(self.x_previous, self.y_previous, self.z_previous))
                self.iterations += 1
                if abs(self.x - self.x_previous) <= self.accuracy and abs(self.y - self.y_previous) <= self.accuracy \
                        and abs(self.z - self.z_previous) <= self.accuracy:
                    self.accuracy = abs(self.x - self.x_previous + self.y - self.y_previous) / 2
                    break
                self.x_previous = self.x
                self.y_previous = self.y
            if self.iterations == 250000:
                self.status = 1

    def get_equations(self, type_eq, x, y, z):
        try:
            if len(self.type_equations) == 2:
                if type_eq == 1:
                    return 0.1 * math.pow(x, 2) + x + 0.2 * math.pow(y, 2) - 0.3
                elif type_eq == 2:
                    return 0.2 * math.pow(x, 2) + y - 0.1 * x * y - 0.7
                elif type_eq == 3:
                    return x + y - math.pow(x, 2) - 5
                elif type_eq == 4:
                    return 3 * y + 2 * math.pow(x, 3) - 2
            else:
                if type_eq == 1:
                    return 2 * math.pow(x, 2) - y + 4 * z
                elif type_eq == 2:
                    return math.sin(x) - math.sin(y) - math.sin(z)
                elif type_eq == 3:
                    return x + math.pow(y, 2) / 2 - 2 * z
                elif type_eq == 4:
                    return 2 * x - 4 * z * y + 5
        except TypeError:
            return self.get_equations(type_eq, x + 1e-7, y + 1e-7, z + 1e-7)
        except ValueError:
            return self.get_equations(type_eq, x + 1e-7, y + 1e-7, z + 1e-7)
        except ZeroDivisionError:
            return self.get_equations(type_eq, x + 1e-7, y + 1e-7, z + 1e-7)

    def get_x_derivative(self, type_eq, x, y, z):
        try:
            if len(self.type_equations) == 2:
                if type_eq == 1:
                    return 0.2 * x + 1
                elif type_eq == 2:
                    return 0.4 * x - 0.1 * y
                elif type_eq == 3:
                    return 1 - 2 * x
                elif type_eq == 4:
                    return 6 * math.pow(x, 2)
            else:
                if type_eq == 1:
                    return 4 * x
                elif type_eq == 2:
                    return math.cos(x)
                elif type_eq == 3:
                    return 1
                elif type_eq == 4:
                    return 2
        except TypeError:
            return self.get_x_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ValueError:
            return self.get_x_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ZeroDivisionError:
            return self.get_x_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)

    def get_y_derivative(self, type_eq, x, y, z):
        try:
            if len(self.type_equations) == 2:
                if type_eq == 1:
                    return 0.4 * y
                elif type_eq == 2:
                    return 1 - 0.1 * x
                elif type_eq == 3:
                    return 1
                elif type_eq == 4:
                    return 3
            else:
                if type_eq == 1:
                    return -1
                elif type_eq == 2:
                    return -math.cos(y)
                elif type_eq == 3:
                    return y
                elif type_eq == 4:
                    return - 4 * z
        except TypeError:
            return self.get_y_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ValueError:
            return self.get_y_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ZeroDivisionError:
            return self.get_y_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)

    def get_z_derivative(self, type_eq, x, y, z):
        try:
            if len(self.type_equations) == 2:
                if type_eq == 1:
                    return 0
                elif type_eq == 2:
                    return 0
                elif type_eq == 3:
                    return 0
                elif type_eq == 4:
                    return 0
            else:
                if type_eq == 1:
                    return 4
                elif type_eq == 2:
                    return -math.cos(z)
                elif type_eq == 3:
                    return - 2
                elif type_eq == 4:
                    return - 4 * y
        except TypeError:
            return self.get_z_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ValueError:
            return self.get_z_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)
        except ZeroDivisionError:
            return self.get_z_derivative(type_eq, x + 1e-9, y + 1e-9, z + 1e-9)

    def get_jacobian(self, x, y, z):
        if len(self.type_equations) == 2:
            return [[self.get_x_derivative(self.type_equations[0], x, y, z),
                     self.get_y_derivative(self.type_equations[0], x, y, z)],
                    [self.get_x_derivative(self.type_equations[1], x, y, z),
                     self.get_y_derivative(self.type_equations[1], x, y, z)]]
        else:
            return [[self.get_x_derivative(self.type_equations[0], x, y, z),
                     self.get_y_derivative(self.type_equations[0], x, y, z),
                     self.get_z_derivative(self.type_equations[0], x, y, z)],
                    [self.get_x_derivative(self.type_equations[1], x, y, z),
                     self.get_y_derivative(self.type_equations[1], x, y, z),
                     self.get_z_derivative(self.type_equations[1], x, y, z)],
                    [self.get_x_derivative(self.type_equations[2], x, y, z),
                     self.get_y_derivative(self.type_equations[2], x, y, z),
                     self.get_z_derivative(self.type_equations[2], x, y, z)]]

    def get_A(self, mode, x, y, z):
        if len(self.type_equations) == 2:
            if mode == 1:
                return [[self.get_equations(self.type_equations[0], x, y, z),
                         self.get_y_derivative(self.type_equations[0], x, y, z)],
                        [self.get_equations(self.type_equations[1], x, y, z),
                         self.get_y_derivative(self.type_equations[1], x, y, z)]]
            elif mode == 2:
                return [[self.get_x_derivative(self.type_equations[0], x, y, z),
                         self.get_equations(self.type_equations[0], x, y, z)],
                        [self.get_x_derivative(self.type_equations[1], x, y, z),
                         self.get_equations(self.type_equations[1], x, y, z)]]
        else:
            if mode == 1:
                return [[self.get_equations(self.type_equations[0], x, y, z),
                         self.get_y_derivative(self.type_equations[0], x, y, z),
                         self.get_z_derivative(self.type_equations[0], x, y, z)],
                        [self.get_equations(self.type_equations[1], x, y, z),
                         self.get_y_derivative(self.type_equations[1], x, y, z),
                         self.get_z_derivative(self.type_equations[1], x, y, z)],
                        [self.get_equations(self.type_equations[2], x, y, z),
                         self.get_y_derivative(self.type_equations[2], x, y, z),
                         self.get_z_derivative(self.type_equations[2], x, y, z)]
                        ]
            elif mode == 2:
                return [[self.get_x_derivative(self.type_equations[0], x, y, z),
                         self.get_equations(self.type_equations[0], x, y, z),
                         self.get_z_derivative(self.type_equations[0], x, y, z)],
                        [self.get_x_derivative(self.type_equations[1], x, y, z),
                         self.get_equations(self.type_equations[1], x, y, z),
                         self.get_z_derivative(self.type_equations[1], x, y, z)],
                        [self.get_x_derivative(self.type_equations[2], x, y, z),
                         self.get_equations(self.type_equations[2], x, y, z),
                         self.get_z_derivative(self.type_equations[2], x, y, z)]]
            elif mode == 3:
                return [[self.get_x_derivative(self.type_equations[0], x, y, z),
                         self.get_y_derivative(self.type_equations[0], x, y, z),
                         self.get_equations(self.type_equations[0], x, y, z)],
                        [self.get_x_derivative(self.type_equations[1], x, y, z),
                         self.get_y_derivative(self.type_equations[1], x, y, z),
                         self.get_equations(self.type_equations[1], x, y, z)],
                        [self.get_x_derivative(self.type_equations[2], x, y, z),
                         self.get_y_derivative(self.type_equations[2], x, y, z),
                         self.get_equations(self.type_equations[2], x, y, z)]]


def printResult(calculator):
    if calculator.status == 0:
        if len(calculator.type_equations) == 2:
            print("\nEquation roots: x=" + str(calculator.x) + ", y=" + str(calculator.y) + "\n" +
                  "Count of iteration: " + str(calculator.iterations) + "\n" +
                  "Calculation error: " + str(calculator.accuracy) + "\n")
            make_graph_2d(calculator)
        else:
            print("\nEquation roots: x=" + str(calculator.x) + ", y=" + str(calculator.y) + ", z=" +
                  str(calculator.z) + "\n" +
                  "Count of iteration: " + str(calculator.iterations) + "\n" +
                  "Calculation error: " + str(calculator.accuracy) + "\n")
            make_graph_3d(calculator)
    elif calculator.status == 1:
        NonLinearEquations.getReadyAnswer(7)


def get_Determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[1][0] *
                matrix[2][1] * matrix[0][2]) \
               - (matrix[0][2] * matrix[1][1] * matrix[2][0] + matrix[0][1] * matrix[1][0] * matrix[2][2] +
                  matrix[0][0] * matrix[1][2] * matrix[2][1])


def make_graph_2d(calculator):
    try:
        ax = plt.gca()
        plt.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title("Graphic of " + str(get_equation_name_2d(calculator.type_equations[0])) + " and \n" +
                  str(get_equation_name_2d(calculator.type_equations[1])))
        x1, y1 = get_eq_2d(calculator.x, calculator.type_equations[0])
        x2, y2 = get_eq_2d(calculator.x, calculator.type_equations[1])
        plt.plot(x1, y1, color="r", linewidth=4)
        plt.plot(x2, y2, color="y", linewidth=4)
        if calculator.type_equations[0] == 1:
            x3, y3 = get_eq_2d(calculator.x, 5)
            plt.plot(x3, y3, color="r", linewidth=4)
        if calculator.type_equations[1] == 1:
            x4, y4 = get_eq_2d(calculator.x, 5)
            plt.plot(x4, y4, color="y", linewidth=4)
        plt.scatter(calculator.x, calculator.y, color="g", s=60)
        plt.show()
        del x1, x2, y1, y2
    except ValueError:
        return
    except ZeroDivisionError:
        return


def get_eq_2d(x, types):
    if types == 1:
        xs = np.linspace(-10.29, 0.29, 100)
        y = list(np.sqrt((-0.1 * np.power(i, 2) - i + 0.3) / 0.2) for i in xs)
        return xs, y
    elif types == 2:
        xs = np.linspace(x - 5, x + 5, 100)
        y = list((-0.2 * np.power(i, 2) + 0.7) / (1 - 0.1 * i) for i in xs)
        return xs, y
    elif types == 3:
        xs = np.linspace(x - 5, x + 5, 100)
        y = list((5 + np.power(i, 2) - i) for i in xs)
        return xs, y
    elif types == 4:
        xs = np.linspace(x - 5, x + 5, 100)
        y = list((2 - 2 * np.power(i, 3)) / 3 for i in xs)
        return xs, y
    elif types == 5:
        xs = np.linspace(-10.29, 0.29, 100)
        y = list((-np.sqrt((-0.1 * np.power(i, 2) - i + 0.3) / 0.2)) for i in xs)
        return xs, y


def make_graph_3d(calculator):
    try:
        x = np.arange(calculator.x - 10, calculator.x + 10, 0.1)
        y = np.arange(calculator.y - 10, calculator.y + 10, 0.1)
        xs, ys = np.meshgrid(x, y)
        z1grid = get_eq_3d(xs, ys, calculator.type_equations[0])
        z2grid = get_eq_3d(xs, ys, calculator.type_equations[1])
        z3grid = get_eq_3d(xs, ys, calculator.type_equations[2])
        fig = pylab.figure()
        axes = Axes3D(fig)
        pylab.title("Graphic of " + str(get_equation_name_3d(calculator.type_equations[0])) + " and \n" +
                    str(get_equation_name_3d(calculator.type_equations[1])) + " and " +
                    str(get_equation_name_3d(calculator.type_equations[2])))
        axes.plot_surface(xs, ys, z1grid, color='r')
        axes.plot_surface(xs, ys, z2grid, color='y')
        axes.plot_surface(xs, ys, z3grid, color='g')
        axes.scatter(calculator.x, calculator.y, calculator.z, s=40)
        pylab.show()
        del xs, ys, z1grid, z2grid, z3grid
    except ValueError:
        return
    except ZeroDivisionError:
        return


def get_eq_3d(x, y, types):
    try:
        if types == 1:
            z = (y - 2 * np.power(x, 2)) / 4
            return z
        elif types == 2:
            z = np.arcsin(np.sin(x) - np.sin(y))
            return z
        elif types == 3:
            z = (x + np.power(y, 2) / 2) / 2
            return z
        elif types == 4:
            z = (2 * x + 5) / (4 * y)
            return z
    except ZeroDivisionError:
        return get_eq_3d(x + 1e-7, y + 1e-7, types)
    except TypeError:
        return get_eq_3d(x + 1e-7, y + 1e-7, types)
    except ValueError:
        return get_eq_3d(x + 1e-7, y + 1e-7, types)


def get_equation_name_2d(type_eq):
    if type_eq == 1:
        return "0.1x^2 + x + 0.2y^2 - 0.3 = 0"
    elif type_eq == 2:
        return "0.2x^2 + y - 0.1xy - 0.7 = 0"
    elif type_eq == 3:
        return "x + y - x^2 - 5 = 0"
    elif type_eq == 4:
        return "3y + 2x^3 - 2 = 0 "


def get_equation_name_3d(type_eq):
    if type_eq == 1:
        return "2x^2 - y + 4z = 0"
    elif type_eq == 2:
        return "sin(x) - sin(y) - sin(z) = 0"
    elif type_eq == 3:
        return "x + y^2 / 2 - 2z = 0"
    elif type_eq == 4:
        return "2x - 4zy + 5 = 0 "
