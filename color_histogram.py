from PIL import Image


def chebyshev(h1, h2):
    '''Compute the Chebyshev distance between two histograms'''
    d = max([abs(x - y) for (x, y) in zip(h1, h2)])
    return d

def normalized_hist(img):
    '''Normalize a histogram'''
    hist = img.histogram()
    px = sum(hist)
    return [i / px for i in hist]

def compare(img1, img2):
    '''Compare images using color histograms'''
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
    import sys, os
    path = sys.argv[1]
    results = []
    os.chdir(path)
    for i in os.listdir():
        for j in os.listdir():
            if i != j:
                if not (j, i) in results:
                    sim = compare(i, j)
                    if sim < 4e-03:
                        results.append((i, j))
    for i in results:
        print(i[0], i[1])
