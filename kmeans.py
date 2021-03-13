#!/usr/bin/python3

################################################################################
# With the shebang above, if the user runs the command 'chmod +x kmeans.py', the
# program can then be run in the following format: './kmeans.py k input.txt'.
# Otherwise, simple run: 'python3 kmeans.py k input.txt'.
################################################################################

import sys
import random
import math
import operator

def euclidean_distance(x_s, y_s):

    sum = 0
    for i in range(len(x_s)):
        sum += math.pow(x_s[i] - y_s[i], 2)
    euclid_dist = math.sqrt(sum)

    return euclid_dist

def initializing_means_to_random_nums(items, k, col_min, col_max):

    feat_size = len(items[0]);
    means = [[0 for i in range(feat_size)] for j in range(k)]

    for mean in means:
        for i in range(len(mean)):
            mean[i] = random.uniform(col_min[i] + 1, col_max[i] - 1)

    return means

def cloumn_max_min_search(items):

    x_pt_length = len(items[0])
    min = [sys.maxsize for i in range(x_pt_length)]
    max = [-sys.maxsize - 1 for i in range(x_pt_length)]

    for x_pt in items:
        for i in range(len(x_pt)):
            if (x_pt[i] < min[i]):
                min[i] = x_pt[i]

            if (x_pt[i] > max[i]):
                max[i] = x_pt[i]

    return min, max

def mean_update(clust_size, mean, x_pt):

    for i in range(len(mean)):
        m = mean[i]
        m = (m * (clust_size - 1) + x_pt[i]) / clust_size
        mean[i] = m

    return mean

def index_builder(x_pt, means):

    index = -1
    minimum = sys.maxsize

    for i in range(len(means)):
        distance = euclidean_distance(x_pt, means[i]);

        if (distance < minimum):
            minimum = distance;
            index = i;

    return index;

def means_calculation(k, lines, items, max_iters = 100):

    col_min, col_max = cloumn_max_min_search(items)
    means = initializing_means_to_random_nums(items, k, col_min, col_max)
    cluster_sizes= [0 for i in range(len(means))]
    is_in = [0 for i in range(len(items))]

    for it in range(max_iters) :
        done = True

        for i in range(len(items)):

            x_pt = items[i]
            index = index_builder(x_pt, means)

            cluster_sizes[index] += 1
            cluster_size = cluster_sizes[index]
            means[index] = mean_update(cluster_size, means[index], x_pt)

            if(index != is_in[i]):
                done = False

            is_in[i] = index

        if (done):
            break

    return means

def cluster_indexing(means, fout, lines, items):

    zipped = zip(lines, items)
    zip_result = sorted(zipped, key = operator.itemgetter(1))

    linez, itemz = zip(*zip_result)

    for e, x_pt in zip(linez, itemz):
        print(e.replace("\t", "   "), "  ", str(index_builder(x_pt, means) + 1))
        print(e.replace("\t", "   "), "  ", str(index_builder(x_pt, means) + 1), file=fout)

def main(argv):

    K = int(sys.argv[1])
    file_name = sys.argv[2]

    fin = open(file_name, 'r')
    lines = fin.read().splitlines()
    fin.close()

    fout = open('output.txt', 'w')

    items = []

    for i in range(len(lines)):
        points_list = lines[i].split()

        item_features = []

        for j in range(len(points_list) - 1):
            values = int(points_list[j])
            item_features.append(values)
        items.append(item_features)

    means = means_calculation(K, lines, items, max_iters = 100)
    cluster_indexing(means, fout, lines, items)

if __name__== "__main__":
    main(sys.argv[1:])
