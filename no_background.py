import cv2 as cv
import numpy as np
import sys

def main():
    fname = sys.argv[1]
    im = cv.imread(fname)

    shape = list(im.shape)
    shape[-1] += 1  # to include alpha channel

    a = np.zeros(shape)

    white = np.array([255, 255, 255])
    tp = np.array([255, 255, 255, 0])

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if all(im[i][j] == white): a[i][j] = tp
            else:
                a[i][j][:-1] = im[i][j]
                a[i][j][-1] = 255

    fname = fname.split('.')[0] + '_no_background.png'
    cv.imwrite(fname, a)

if __name__ == '__main__':
    main()
