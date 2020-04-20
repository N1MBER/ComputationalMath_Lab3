import math
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class Qualifier:
    type_solve = 0
    type_equations = 0
    a = 0
    b = 0
    accuracy = 0

    def __init__(self, type_solve):
        self.type_solve = type_solve
        self.choose_Equations()
        self.defining_Boundaries()
        self.defining_Accuracy()
        self.start_of_calculation()

    def choose_Equations(self):
        while 1:
            try:
                print("\nPlease choose a equations:\n"
                      "\t1. x^2 - 2 = 0\n"
                      "\t2. 5/x - 2x = 0\n"
                      "\t3. e^2x - 2\n"
                      "\t4. x^3 - x + 4 = 0\n")
                answer = int(input("Variant: ").strip())
                if answer == 1:
                    self.type_equations = 1
                    break
                elif answer == 2:
                    self.type_equations = 2
                    break
                elif answer == 3:
                    self.type_equations = 3
                    break
                elif answer == 4:
                    self.type_equations = 4
                    break
                else:
                    getReadyAnswer(1)
                    continue
            except TypeError:
                getReadyAnswer(1)
                continue

    def defining_Boundaries(self):
        while 1:
            try:
                print("Please input a border of segment, example: -10 10.\n")
                limits = list(input("Border of segment: ").strip().split(" "))
                if len(limits) == 2 and (float(limits[0].strip()) < float(limits[1].strip())):
                    self.a = float(limits[0].strip())
                    self.b = float(limits[1].strip())
                    break
                else:
                    getReadyAnswer(1)
                    continue
            except TypeError:
                getReadyAnswer(1)

    def defining_Accuracy(self):
        while 1:
            try:
                print("\nPlease input accuracy of calculation.\n")
                accuracy = float(input("Accuracy: ").strip())
                if accuracy <= 0:
                    getReadyAnswer(1)
                    continue
                else:
                    self.accuracy = accuracy
                    break
            except TypeError:
                getReadyAnswer(1)

    def start_of_calculation(self):
        calculator = Calculator(self.type_equations, self.a, self.b, self.accuracy, self.type_solve)
        calculator.calculate()
        printResult(calculator)
        del calculator


class Calculator:
    status = 0
    solvable = 1
    mode_solve = 0
    type_equations = 0
    a = 0
    b = 0
    steps = 0
    previous_count = 0
    accuracy = 0
    result = 0
    segments = []

    def __init__(self, type_equations, a, b, accuracy, mode_solve):
        self.type_equations = type_equations
        self.a = a
        self.segments = []
        self.steps = 0
        self.solvable = 1
        self.status = 0
        self.previous_count = 0
        self.result = 0
        self.b = b
        self.accuracy = accuracy
        self.mode_solve = mode_solve

    def calculate(self):
        self.result = self.b
        if self.check_derivative():
            if self.get_Solve_Value(self.a) * self.get_Solve_Value(self.b) < 0:
                if self.mode_solve == 1:
                    while 1:
                        self.steps += 1
                        if self.solvable and (self.steps < 2500000):
                            self.get_Solve_Tangent()
                            count_x = [self.result, self.previous_count]
                            count_y = [0, self.get_Solve_Value(self.previous_count)]
                            segment = [count_x, count_y]
                            self.segments.append(segment)
                            if abs(self.result - self.previous_count) < self.accuracy and abs(
                                    self.get_Solve_Value(self.result)) < self.accuracy and (
                                    self.a <= self.result <= self.b):
                                self.accuracy = abs(self.result - self.previous_count)
                                break
                            else:
                                continue
                        else:
                            if self.steps == 2500000:
                                self.status = 3
                            else:
                                self.status = 1
                            break
                elif self.mode_solve == 2:
                    while 1:
                        self.steps += 1
                        if self.solvable and (self.steps < 2500000):
                            count_x = [self.result, self.a]
                            count_y = [self.get_Solve_Value(self.result), self.get_Solve_Value(self.a)]
                            segment = [count_x, count_y]
                            self.segments.append(segment)
                            self.get_Solve_Chord()
                            if abs(self.result - self.previous_count) < self.accuracy and abs(
                                    self.get_Solve_Value(self.result)) < self.accuracy and (
                                    self.a <= self.result <= self.b):
                                self.accuracy = abs(self.result - self.previous_count)
                                break
                        else:
                            if self.steps == 2500000:
                                self.status = 3
                            else:
                                self.status = 1
                            break
            else:
                self.status = 2

    def check_derivative(self):
        float_range = np.arange(self.a, self.b, (self.b - self.a) / 100)
        convergence = 1
        flag = 0
        if self.get_derivative(self.a) < 0:
            flag = 1
        else:
            flag = 0
        previous_flag = flag
        for i in float_range:
            if self.get_derivative(i) < 0:
                flag = 1
            else:
                flag = 0
            if previous_flag != flag:
                convergence = 0
                break
            previous_flag = flag
        if self.get_second_derivative(self.a) < 0:
            flag = 1
        else:
            flag = 0
        previous_flag = flag
        for i in float_range:
            if self.get_second_derivative(i) < 0:
                flag = 1
            else:
                flag = 0
            if previous_flag != flag:
                convergence = 0
                break
            previous_flag = flag
        return convergence

    def get_Solve_Value(self, x):
        try:
            if self.type_equations == 1:
                return math.pow(x, 2) - 2
            elif self.type_equations == 2:
                return 5 / x - 2 * x
            elif self.type_equations == 3:
                return math.pow(math.e, 2 * x) - 2
            elif self.type_equations == 4:
                return math.pow(x, 3) - x + 4
        except ZeroDivisionError:
            return self.get_Solve_Value(x + 1e-8)

    def get_derivative(self, x):
        try:
            if self.type_equations == 1:
                return 2 * x
            elif self.type_equations == 2:
                return -5 / (math.pow(x, 2)) - 2
            elif self.type_equations == 3:
                return 2 * math.pow(math.e, 2 * x)
            elif self.type_equations == 4:
                return 3 * math.pow(x, 2) - 1
        except ZeroDivisionError:
            return self.get_derivative(x + 1e-8)

    def get_second_derivative(self, x):
        try:
            if self.type_equations == 1:
                return 2
            elif self.type_equations == 2:
                return 10 / (math.pow(x, 3))
            elif self.type_equations == 3:
                return 4 * math.pow(math.e, 2 * x)
            elif self.type_equations == 4:
                return 6 * x
        except ZeroDivisionError:
            return self.get_second_derivative(x + 1e-8)

    def get_Solve_Chord(self):
        try:
            count = self.result
            self.result = self.result - ((self.a - self.result) * self.get_Solve_Value(self.result)) / (
                    self.get_Solve_Value(self.a) - self.get_Solve_Value(self.result))
            self.previous_count = count
            if self.a * self.result < 0:
                self.b = self.result
            elif self.result * self.b < 0:
                self.a = self.result
        except ValueError:
            self.result = self.result - ((self.a - self.result) * self.get_Solve_Value(self.result)) / (
                    self.get_Solve_Value(self.a) - self.get_Solve_Value(self.result))
        except TypeError:
            self.result = self.result - ((self.a - self.result) * self.get_Solve_Value(self.result)) / (
                    self.get_Solve_Value(self.a) - self.get_Solve_Value(self.result))
        except ZeroDivisionError:
            self.result = self.result - ((self.a - self.result) * self.get_Solve_Value(self.result + 1e-8)) / (
                    self.get_Solve_Value(self.a) - self.get_Solve_Value(self.result + 1e-8))

    def get_Solve_Tangent(self):
        try:
            self.previous_count = self.result
            self.result = self.result - self.get_Solve_Value(self.result) / self.get_derivative(self.result)
        except TypeError:
            self.result = self.result - self.get_Solve_Value(self.result + 1e-8) / self.get_derivative(
                self.result + 1e-8)
        except ValueError:
            self.result = self.result - self.get_Solve_Value(self.result + 1e-8) / self.get_derivative(
                self.result + 1e-8)
        except ZeroDivisionError:
            self.result = self.result - self.get_Solve_Value(self.result + 1e-8) / self.get_derivative(
                self.result + 1e-8)


def printResult(calculator):
    if calculator.solvable == 1:
        if calculator.status == 0:
            print("\nEquation root: " + str(calculator.result) + "\n" +
                  "Count of iteration: " + str(calculator.steps) + "\n" +
                  "Calculation error: " + str(calculator.accuracy) + "\n")
            make_graph(calculator)
        elif calculator.status == 1:
            getReadyAnswer(3)
        elif calculator.status == 2:
            getReadyAnswer(4)
        elif calculator.status == 3:
            getReadyAnswer(5)
        elif calculator.status == 4:
            getReadyAnswer(6)
    else:
        getReadyAnswer(2)


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("Incorrect input.\n")
    elif type_answer == 2:
        print("No solution.\n")
    elif type_answer == 3:
        print("There is no concrete solution or it doesn't exist.\n")
    elif type_answer == 4:
        print("Convergence condition is not satisfied on this segment.\n")
    elif type_answer == 5:
        print("Counts of iteration reached 2.5 million , solution not found.\n")
    elif type_answer == 6:
        print("The initial approximation is poorly selected, solution not found.\n")
    elif type_answer == 7:
        print("Counts of iteration reached 250 thousand , solution not found.\n")


def make_graph(calculator):
    try:
        x = np.linspace(calculator.a, calculator.b, 100)
        equations = {1: ["f(x) = x^2 - 2", [(math.pow(i, 2) - 2) for i in x]],
                     2: ["f(x) = 5/x - 2x", [(5 / i - 2 * i) for i in x]],
                     3: ["f(x) = e^2x - 2", [(math.pow(math.e, 2 * i) - 2) for i in x]],
                     4: ["f(x) = x^3 - x + 4", [(math.pow(i, 3) - i + 4) for i in x]]}

        ax = plt.gca()
        plt.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title("Graphic of " + equations[calculator.type_equations][0])
        plt.plot(x, 0 * x, color="black", linewidth=2)
        for segment in calculator.segments:
            if calculator.a <= segment[0][0] <= calculator.b and calculator.a <= segment[0][1] <= calculator.b:
                plt.plot(segment[0], segment[1], color="b")
        plt.plot(x, equations[calculator.type_equations][1], color="r", linewidth=4)
        plt.scatter(calculator.result, 0, color="g", s=60)
        plt.show()
        del x
    except ValueError:
        return
    except ZeroDivisionError:
        return
