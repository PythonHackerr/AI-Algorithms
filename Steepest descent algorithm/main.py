from gradient import gradient_descent, x
from lr_tests import test_different_lrs_func_f, test_different_lrs_func_g
import gradient as grad
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.style.use('dark_background')

    guesses = gradient_descent(grad.func_f, grad.df, [-0.5], 500, 0.001)
    minimum = guesses[len(guesses) - 1]
    print (f"minimum of the function f: ({minimum})");
    grad.plot_func_f(x, grad.func_F)
    for guess in guesses:
        plt.plot(guess[0], guess[1], 'o', color='red');



    guesses = gradient_descent(grad.func_g, grad.dg, [-0.2,0.5], 200, 0.005)
    minimum = guesses[len(guesses) - 1]
    print (f"minimum of the function g: ({minimum})");

    start, stop, n_values = -3.0, 3.0, 100

    x_values = np.linspace(start, stop, n_values)
    y_values = np.linspace(start, stop, n_values)

    X,Y = np.meshgrid(x_values, y_values)
    Z = grad.get_func_g(X, Y) # evaluation of the function on the grid
    grad.plot_func_g(X, Y, Z)

    for guess in guesses:
        plt.plot(guess[0], guess[1], 'o', color='red');

    
    
    plt.show()
 

if __name__=="__main__":
    main()
    # test_different_lrs_func_f()
    # test_different_lrs_func_g()