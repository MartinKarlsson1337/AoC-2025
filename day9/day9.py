import numpy as np

if __name__ == '__main__':
    data = np.loadtxt("day9/day9.txt", delimiter=",", dtype=np.int64)
    x, y = data[:, 0], data[:, 1]

    sorted_x = np.argsort(x)
    sorted_y = np.argsort(y)

    x_bounds = np.array([x[sorted_x][0], x[sorted_x][1]])
    y_bounds = np.array([y[sorted_y][0], x[sorted_y][1]])

    data = data - np.array([x_bounds[0], y_bounds[0]])

    print(data)

