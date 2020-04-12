import math

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
                      "\t1. x^3 - 6x + 2 = 0\n"
                      "\t2. sqrt(x + 1) - 1/x = 0\n"
                      "\t3. x^2 - 20sin(x)\n"
                      "\t4. x^3 - 2x^2 - 4x + 7 = 0\n")
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
                if len(limits) == 2:
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
    solvable = 1
    mode_solve = 0
    type_equations = 0
    a = 0
    b = 0
    steps = 0
    previous_count = 0
    accuracy = 0
    result = 0

    def __init__(self, type_equations, a, b, accuracy, mode_solve):
        self.type_equations = type_equations
        self.a = a
        self.b = b
        self.accuracy = accuracy
        self.mode_solve = mode_solve

    def calculate(self):
        self.result = self.b
        if self.mode_solve == 1:
            while 1:
                self.steps += 1
                if self.solvable or (self.steps < 50000):
                    self.get_Solve_Tangent()
                    if abs(self.result - self.previous_count) < self.accuracy:
                        self.accuracy = abs(self.result - self.previous_count)
                        break
                    else:
                        continue
                else:
                    break
        elif self.mode_solve == 2:
            while 1:
                self.steps += 1
                if self.solvable or (self.steps < 50000):
                    self.get_Solve_Chord()
                    if abs(self.result - self.previous_count) < self.accuracy:
                        self.accuracy = abs(self.result - self.previous_count)
                        break
                else:
                    break
        else:
            getReadyAnswer(1)

    def get_Solve_Chord(self):
        try:
            self.previous_count = self.result
            if self.type_equations == 1:
                self.result = self.result - ((self.a - self.result) *
                                             (math.pow(self.result, 3) - 6 * self.result + 2)) / \
                              ((math.pow(self.a, 3) - 6 * self.a + 2) -
                               (math.pow(self.result, 3) - 6 * self.result + 2))
            elif self.type_equations == 2:
                self.result = self.result - ((self.a - self.result) *
                                             (math.sqrt(self.result + 1) - 1 / self.result)) / \
                              ((math.sqrt(self.a + 1) - 1 / self.a) - (math.sqrt(self.result + 1) - 1 / self.result))
            elif self.type_equations == 3:
                self.result = self.result - ((self.a - self.result) *
                                             (math.pow(self.result, 2) - 20 * math.sin(self.result))) / \
                              ((math.pow(self.a, 2) - 20 * math.sin(self.a)) - (
                                      math.pow(self.result, 2) - 20 * math.sin(self.result)))
            elif self.type_equations == 4:
                self.result = self.result - ((self.a - self.result) * (
                        math.pow(self.result, 3) - 2 * math.pow(self.result, 2) - 4 * self.result + 7)) / \
                              ((math.pow(self.a, 3) - 2 * math.pow(self.a, 2) - 4 * self.a + 7) - (
                                      math.pow(self.result, 3) - 2 * math.pow(self.result, 2) - 4 * self.result + 7))
            else:
                getReadyAnswer(1)
            if self.a * self.result < 0:
                self.b = self.result
            elif self.result * self.b < 0:
                self.a = self.result
        except ValueError:
            self.solvable = 0
        except TypeError:
            self.solvable = 0

        # Useless method. Don't work with any count.
        # try:
        #     self.previous_count = self.result
        #     if self.type_equations == 1:
        #         self.result = (self.a * (math.pow(self.b, 3) - 6 * self.b + 2) - self.b *
        #         (math.pow(self.a, 3) - 6 * self.a + 2)) / \
        #                       ((math.pow(self.b, 3) - 6 * self.b + 2) - (math.pow(self.a, 3) - 6 * self.a + 2))
        #     elif self.type_equations == 2:
        #         self.result = (self.a * (math.sqrt(self.b + 1) - 1 / self.b) - self.b * (
        #                 math.sqrt(self.a + 1) - 1 / self.a)) / \
        #                       ((math.sqrt(self.b + 1) - 1 / self.b) - (math.sqrt(self.a + 1) - 1 / self.a))
        #     elif self.type_equations == 3:
        #         self.result = (self.a * (math.pow(self.b, 2) - 20 * math.sin(self.b)) - self.b * (
        #                 math.pow(self.a, 2) - 20 * math.sin(self.a))) / \
        #                       ((math.pow(self.b, 2) - 20 * math.sin(self.b)) -
        #                       (math.pow(self.a, 2) - 20 * math.sin(self.a)))
        #     elif self.type_equations == 4:
        #         self.result = (self.a * (math.pow(self.b, 3) - 2 * math.pow(self.b, 2) - 4 * self.b + 7) - self.b * (
        #                 math.pow(self.a, 3) - 2 * math.pow(self.a, 2) - 4 * self.a + 7)) / \
        #                       ((math.pow(self.b, 3) - 2 * math.pow(self.b, 2) - 4 * self.b + 7) - (
        #                               math.pow(self.a, 3) - 2 * math.pow(self.a, 2) - 4 * self.a + 7))
        #     else:
        #         getReadyAnswer(1)
        #     if self.a * self.result < 0:
        #         self.b = self.result
        #     elif self.result * self.b < 0:
        #         self.a = self.result
        # except ValueError:
        #     self.solvable = 0
        # except TypeError:
        #     self.solvable = 0

    def get_Solve_Tangent(self):
        try:
            self.previous_count = self.result
            if self.type_equations == 1:
                self.result = self.result - (math.pow(self.result, 3) - 6 * self.result + 2) / (
                        3 * math.pow(self.result, 2) - 6)
            elif self.type_equations == 2:
                self.result = self.result - (math.sqrt(self.result + 1) - 1 / self.result) / (
                        1 / (2 * math.sqrt(self.result + 1)) + 1 / (math.pow(self.result, 2)))
            elif self.type_equations == 3:
                self.result = self.result - (math.pow(self.result, 2) - 20 * math.sin(self.result)) / (
                        2 * self.result - 20 * math.cos(self.result))
            elif self.type_equations == 4:
                self.result = self.result - (
                        math.pow(self.result, 3) - 2 * math.pow(self.result, 2) - 4 * self.result + 7) / (
                                      3 * math.pow(self.result, 2) - 4 * self.result - 4)
            else:
                getReadyAnswer(1)
        except ValueError:
            self.solvable = 0
        except TypeError:
            self.solvable = 0


def printResult(calculator):
    if calculator.solvable == 1:
        print("\nEquation root: " + str(calculator.result) + "\n" +
              "Count of iteration: " + str(calculator.steps) + "\n" +
              "Calculation error: " + str(calculator.accuracy) + "\n")
    else:
        getReadyAnswer(1)


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("Incorrect input.\n")
