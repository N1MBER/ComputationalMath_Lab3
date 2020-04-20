from Solver import NonLinearEquations
from Solver import NonLinearSystems

print("Welcome to non linear solver!")

while 1:
    print("What you want?\n"
          "\t1. Solve non linear equations.\n"
          "\t2. Solve non linear system.\n"
          "\t3. Exit\n")
    try:
        answer = int(input("Please choose a variant: ").strip())
        if answer == 1:
            while 1:
                print("Please choose method of solution:\n"
                      "\t1. Method of tangent.\n"
                      "\t2. Method of chord.\n"
                      "\t3. Back\n")
                eq = float(input("Please choose a variant: ").strip())
                if eq == 1:
                    qualifier = NonLinearEquations.Qualifier(1)
                    del qualifier
                    continue
                elif eq == 2:
                    qualifier = NonLinearEquations.Qualifier(2)
                    del qualifier
                    continue
                elif eq == 3:
                    break
        elif answer == 2:
            while 1:
                print("1. Continue.\n"
                      "2. Back.\n")
                sys = float(input("Please choose a variant: ").strip())
                if sys == 1:
                    qualifier = NonLinearSystems.Qualifier()
                    del qualifier
                    continue
                elif sys == 2:
                    break
        elif answer == 3:
            print("Exit...")
            break
    except TypeError:
        NonLinearEquations.getReadyAnswer(1)
        continue
    except ValueError:
        NonLinearEquations.getReadyAnswer(1)
        continue
    except KeyboardInterrupt:
        print("Exit...")
        break
