from gradient import gradient_descent, func_f, func_g, df, dg

def test_different_lrs_func_f():
    x_values = [-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]
    lr_values = [0.00005, 0.0005, 0.001, 0.0025, 0.005, 0.0075, 0.01, 0.0175, 0.025, 0.05, 0.1]
    for start_x in x_values:
        print(f"\nStart_x: {start_x}")
        for lr in lr_values:
            try:
                guesses = gradient_descent(func_f, df, [start_x], 1000, lr)
                minimum_x = guesses[len(guesses) - 1][0]
                real_minimum1 = -1.412370614477653
                real_minimum2 = 1.0125586528323918
                diff = min(abs(minimum_x-real_minimum1), abs(minimum_x-real_minimum2))
                if (diff > 0.0001):
                    print(f"Lr is too LOW / High: {lr}, difference is {diff}")
                else:
                    print(f"OK for lr: {lr}")
            except:
                print(f"Lr is too HIGH: {lr}")

def test_different_lrs_func_g():

    xy_values = [-3, -2, -1, 0, 1, 2, 3]
    lr_values = [0.00005, 0.0005, 0.001, 0.0025, 0.005, 0.0075, 0.01, 0.0175, 0.025, 0.05, 0.1]
    for start_x in xy_values:
        for start_y in xy_values:
            print(f"\nStart_coords: ({start_x}, {start_y})")
            for lr in lr_values:
                try:
                    guesses = gradient_descent(func_g, dg, [start_x, start_y], 1000, lr)
                    minimum_x = guesses[len(guesses) - 1][0]
                    real_minimum1 = -1.412370614477653
                    real_minimum2 = 1.0125586528323918
                    diff = min(abs(minimum_x-real_minimum1), abs(minimum_x-real_minimum2))
                    if (diff > 0.0001):
                        print(f"Lr is too LOW for: {lr}, difference is {diff}")
                    else:
                        print(f"OK for: {lr}")
                except:
                    print(f"Lr is too HIGH: {lr}")
