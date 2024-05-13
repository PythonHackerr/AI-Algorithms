import numpy as np
import matplotlib.pyplot as plt
 
class WrongLearningRate(Exception):
    pass

x = np.linspace(-6, 6, 100)

def plot_func_f(x, y):
    fig = plt.figure(figsize = (12, 8))

    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, color='blue', label ='10*x^4 + 3*x^3 - 30*x^2 + 10*x')
    plt.legend()
    plt.grid(True, linestyle =':')
    plt.xlim([-5, 5])
    plt.ylim([-80, 80])

    plt.title('Gradient descent for finding minima of function')
  
    plt.xlabel("X")
    plt.ylabel("Y")


def plot_func_g(x, y, z):
    fig = plt.figure(figsize = (10, 10))
    graph = plt.contour(x, y, z, 50)
    plt.clabel(graph,inline=1,fontsize=10)


func_F = 10*x**4 + 3*x**3 - 30*x**2 + 10*x


func_f = [[10,3,-30,10,0]]
func_g = [[10,3,-30,10,0], [10,0,0,0,0]]

df = [[40,9,-60,10]]
dg = [[40,9,-60,10], [40,0,0,0]]


def get_func_f(x):
    return 10*x**4 + 3*x**3 - 30*x**2 + 10*x

def get_func_g(x, y):
    return 10*y**4 + 10*x**4 + 3*x**3 - 30*x**2 + 10*x


def eval_df(df, coords):
    try:
        result = []
        temp_result = 0
        for i in range(len(coords)):
            temp_result = 0;
            for j in range(len(df[i])):
                temp_result += df[i][j] * (coords[i] ** (len(df[i])-1-j))
            result.append(temp_result)

    except OverflowError:
        raise WrongLearningRate("Try with different learning rate value")
    return result


def eval_f(f, coords):
    try:
        result = 0
        for i in range(len(coords)):
            for j in range(len(f[i])):
                result += f[i][j] * (coords[i] ** (len(f[i])-1-j))
    except OverflowError:
        raise WrongLearningRate("Try with different learning rate value")
    return result



def gradient_descent(f, df, start_coords, iterations = 1000, learning_rate = 0.001):
    guesses_coords = []
    curr_coords = start_coords;

    for i in range(iterations):
        prev_coords = curr_coords
        for j in range(len(curr_coords)):
            curr_coords[j] -= learning_rate * eval_df(df, prev_coords)[j]
        
        if (len(curr_coords) == 1):
            guesses_coords.append([curr_coords[0], eval_f(f, curr_coords)])
        else:
            guesses_coords.append([curr_coords[0], curr_coords[1], eval_f(f, curr_coords)])
        
        # guesses_coords.append(curr_coords)
    return guesses_coords