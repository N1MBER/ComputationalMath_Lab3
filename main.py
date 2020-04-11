import logic

print("Welcome to not linear solver!")

while 1:
    print("Please choose method of solution:\n"
          "\t1. Method of tangent.\n"
          "\t2. Method of chord.\n"
          "\t3. Exit\n")
    try:
        answer = float(input("Please choose a variant: ").strip())
        if answer == 1:
            qualifier = logic.Qualifier(1)
            del qualifier
            continue
        elif answer == 2:
            qualifier = logic.Qualifier(2)
            del qualifier
            continue
        elif answer == 3:
            print("Exit...")
            break
    except TypeError:
        logic.getReadyAnswer(1)
        continue
    except ValueError:
        logic.getReadyAnswer(1)
        continue
    except KeyboardInterrupt:
        print("Exit...")
        break
