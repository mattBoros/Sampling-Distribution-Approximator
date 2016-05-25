import time
from matplotlib import pyplot
from save_stack_heights_using_jar import get_stack_heights
import PATHS


def save_sampling_distribution_image(sample_size, path):
    print(get_stack_heights(sample_size))
    time.sleep(1.8)
    xs = []
    ys = []

    with open(PATHS.stack_heights) as f:
        for line in f:
            x, y = line.split(' ')
            xs.append(float(x))
            ys.append(int(y))

    #normalize
    xs = [2*x - 1 for x in xs]
    x_width = 2/len(xs)
    sum_of_ys = sum(x_width*y for y in ys)
    ys = list(map(lambda i: pow(i/sum_of_ys, 0.5), ys))


    pyplot.plot(xs, ys)
    pyplot.savefig(path)
    pyplot.close()












