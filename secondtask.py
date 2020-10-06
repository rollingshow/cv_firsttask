import matplotlib.pyplot as plt
import numpy as np


def get_coords(filename):
    # Считываем реальный размер
    size = np.genfromtxt(filename, max_rows=1, deletechars="\n")
    # Считаываем массив
    array = np.genfromtxt(filename, skip_header=2, delimiter=" ", deletechars="\n", dtype="uint8")
    # Логическое или для осей
    row = np.any(array, axis=0)
    col = np.any(array, axis=1)

    first_r = 10000; last_r = -10000
    first_c = 10000; last_c = -10000
    for i, elem in enumerate(row):
        if(elem != 0):
            if (first_r > i): first_r = i
            if (last_r < i): last_r = i

    for i, elem in enumerate(col):
        if(elem != 0):
            if (first_c > i): first_c = i
            if (last_c < i): last_c = i

    return {"first_r": first_r, "last_r": last_r, "first_c": first_c, "last_c": last_c}

i1 = get_coords("img1.txt")
i2 = get_coords("img2.txt")

print(i2["first_r"] - i1["first_r"], " ", i2["first_c"] - i1["first_c"])