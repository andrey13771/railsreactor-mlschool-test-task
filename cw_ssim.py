from PIL import Image
import os
import numpy as np


k = 0.01


def cw_ssim(a, b, width = 30):
    widths = np.arange(1, width + 1)
    a = np.asarray(a.getdata())
    b = np.asarray(b.getdata())
    cwtmatr1 = []
    cwtmatr2 = []
    for i in widths:
        length = min(10 * i, len(a))
        conv1 = np.convolve(a, mexican_hat(length, i), mode = 'same')
        conv2 = np.convolve(b, mexican_hat(length, i), mode = 'same')
        cwtmatr1.append(conv1)
        cwtmatr2.append(conv2)
    cwtmatr1 = np.asarray(cwtmatr1)
    cwtmatr2 = np.asarray(cwtmatr2)
#    print('cwt1',cwtmatr1)
#    print('cwt2',cwtmatr2)
    c1c2 = np.multiply(abs(cwtmatr1), abs(cwtmatr2))
    c1_2 = np.square(abs(cwtmatr1))
    c2_2 = np.square(abs(cwtmatr2))
    x1 = 2 * np.sum(c1c2, axis = 0) + k
    y1 = np.sum(c1_2, axis =0) + np.sum(c2_2, axis = 0) + k
    c1c2_conj = np.multiply(cwtmatr1, np.conjugate(cwtmatr2))
    x2 = 2 * np.abs(np.sum(c1c2_conj, axis = 0)) + k
    y2 = 2 * np.sum(np.abs(c1c2_conj), axis = 0) + k
    ssim = (x1 / y1) * (x2 / y2)
#    print('ssim', ssim)
    av = np.average(ssim)
#    print('av', av)
    return av

def compare(img1, img2):
    a = Image.open(img1).convert('L')
    b = Image.open(img2).convert('L')
    if a == b:
        return 1
    a = a.resize((1024, 768), Image.ANTIALIAS)
    b = b.resize((1024, 768), Image.ANTIALIAS)
    sim = cw_ssim(a, b)
    return sim

def mexican_hat(t, sig):
    A = 2 / (np.sqrt(3 * sig) * np.pi ** (1 / 4))
    B = np.add(np.negative(np.divide(np.square(t), sig ** 2)), 1)
    C = np.exp(np.negative(np.divide(np.square(t), 2 * sig ** 2)))
    D = np.multiply(np.multiply(A, B), C)
    return D




if __name__ == '__main__':
    import sys, os
    path = sys.argv[1]
    results = []
    os.chdir(path)
    for i in os.listdir():
        for j in os.listdir():
            if i != j:
                if not (j, i) in results:
                    sim = compare(i, j)
                    if sim > 0.8:
                        results.append((i, j))
    for i in results:
        print(i[0], i[1])
