import numpy as np
import cv2 as cv2


class gaborFilter:

    def build_filters(self):
        filters = []
        ksize = 31
        for theta in np.arange(0, np.pi, np.pi / 32):
            params = {'ksize': (ksize, ksize), 'sigma': 1.0, 'theta': theta,
                      'lambd': 15.0, 'gamma': 0.02, 'psi': 0,
                      'ktype': cv2.CV_32F}
        kern = cv2.getGaborKernel(**params)
        kern /= 1.5*kern.sum()
        filters.append((kern, params))
        return filters

    def process(self, img, filters):
        results = []
        for kern, params in filters:
            fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
            results.append[fimg]
        return results
