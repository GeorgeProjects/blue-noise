from blue_noise import blueNoise
import time
import csv
import json
from itertools import islice
import logging

if __name__ == '__main__':
    for r in [200000, 100000, 25000, 6000, 1250, 300, 100, 50, 20]:
        t1 = time.time()
        points = []
        with open('./proj_point_list.csv', 'r', encoding='utf-8') as f:
            csvF = csv.reader(f)
            for row in islice(csvF, 1, None):
                index = row[0]
                x = float(row[1])
                y = float(row[2])
                points.append({'index': index, 'x': x, 'y': y})

        samplePoints = blueNoise(points, r)

        recentBlueNoiseFilePath = './samplePoints-{0}-{1}-{2}.json'.format(r, len(samplePoints),
                                                                           len(samplePoints) / len(
                                                                               points))
        print('samplePoints num', len(samplePoints))

        with open(recentBlueNoiseFilePath, 'w',
                  encoding='utf-8') as f:
            logging.info(str(r) + ' sampling over,' + str((time.time() - t1) / 60))
            logging.info('-------------------')
            f.write(json.dumps(samplePoints))
