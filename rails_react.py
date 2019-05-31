from PIL import Image
import os
import numpy as np


def chebyshev(h1, h2):
    d = max([abs(x - y) for (x, y) in zip(h1, h2)])
    return d

def normalized_hist(img):
    hist = img.histogram()
    px = sum(hist)
    return [i / px for i in hist]

def compare(img1, img2):
    a = Image.open(img1)
    b = Image.open(img2)
    if a == b:
        return 0
    a = a.convert('L')
    b = b.convert('L')
    h1 = normalized_hist(a)
    h2 = normalized_hist(b)
    d = chebyshev(h1, h2)
    return d








if __name__ == '__main__':
#    import sys
#    path = sys.argv[1]
    results = []
    path = 'c://users/johntitor/downloads/dev_dataset/'
    for i in os.listdir(path = path):
        for j in os.listdir(path = path):
            if i != j:
                if not (j, i) in results:
                    sim = compare(path + i, path + j)
                    if sim < 4e-03:
                        results.append((i, j))
    for i in results:
        print(i[0], i[1])
##                if results.get(i, ''):
##                    results[i].append((j, sim))
##                else:
##                    results[i] = [(j, sim)]
