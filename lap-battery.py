#!/usr/bin/python

import sys
import itertools
x = []
y = []
val = []
def main():

    fd = open("trainingdata.txt", "r")
    contents = fd.readlines()
    data = []
    n = 0
    for line in contents:
        hr_in = line.split(",")
        val = [float(hr_in[0]), float(hr_in[1])]
        if val[1] != 8.0:
            data.append(val)
            n += 1
    data = sorted(data)
    val = [sum(x) for x in zip(*data)]
    sum_x = val[0]
    sum_y = val[1]
    xy = []
    for item in data:
            xy.append(item[0] * item[1])
    x_square = []
    for item in data:
        x_square.append( item[0] * item[0])
    sum_x_sqare = sum(x_square)
    sum_xy = sum(xy)
    a = ((sum_y * sum_x_sqare) - (sum_x * sum_xy)) / ((n * sum_x_sqare) - (sum_x * sum_x))
    b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_sqare) - (sum_x * sum_x))
    get_input = float(raw_input().strip())
    get_input_val = float(get_input)
    data = sorted(data, reverse=True)
    val = data[0]
    val = val[0]
    if get_input_val > val:
        print 8.0
    else:
        output = (get_input_val * b ) + a
        output = str(round(output, 2))
        print output
#main
if __name__ == '__main__':
    main()
