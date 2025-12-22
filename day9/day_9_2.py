import numpy as np
from shapely.geometry import Polygon, box
from tqdm.auto import tqdm
from itertools import combinations

if __name__ == '__main__':
    data = np.loadtxt("day9/day9.txt", delimiter=",", dtype=np.int64)
    data_length = data.shape[0]

    polygon = Polygon(data)

    def check_rectangle(p1, p2):
        x_min, y_min = np.minimum(p1, p2)
        x_max, y_max = np.maximum(p1, p2)
        rect = box(x_min, y_min, x_max, y_max)

        return polygon.covers(rect)

    def get_area(p1, p2):
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

    max_area = 0

    for p1, p2 in tqdm(combinations(data, 2), total=data_length**2):
        if check_rectangle(p1, p2):
            area = get_area(p1, p2)
            if area > max_area:
                max_area = area

    print(max_area)