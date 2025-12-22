import numpy as np

if __name__ == '__main__':
    data = np.loadtxt("day9/day9.txt", delimiter=",", dtype=np.int64)
    x, y = data[:, 0], data[:, 1]
    data_length = data.shape[0]

    x = np.abs(x[None, :] - x[:, None])
    y = np.abs(y[None, :] - y[:, None])

    areas = (x + 1) * (y + 1)

    sorted_areas = np.argsort(areas.ravel())[::-1]
    
    max_area = areas.ravel()[sorted_areas[0]]

    print(max_area)
