import numpy as np

from src.filters import minucias


def _get_core(minutae: np.array):
    return [point for point in minutae if point[2] == minucias.MnType.Core][0]


def _extract_radial(minutae: np.array,
                    bucketsize: int):
    core = _get_core(minutae)
    if core is None:
        raise Exception('missing core point for polar method')

    feat = []
    for i in range(0, 360//bucketsize):
        feat.append({minucias.MnType.Termination: 0,
                     minucias.MnType.Bifurcation: 0})
    for point in minutae:
        i, j, t, _ = point if len(point) == 4 else point + (None,)
        if (t == minucias.MnType.Termination or t == minucias.MnType.Bifurcation) \
                and not (i == core[0] and j == core[1]):
            h = float(abs(i - core[0]))
            w = float(abs(j - core[1]))

            angle = None
            if i < core[0]:
                if j > core[1]:  # 1st quarter
                    angle = int(np.rad2deg(np.arctan(h/w)))
                elif j < core[1]:  # 2nd quarter
                    angle = int(np.rad2deg(np.arctan(w/h))) + 90
                else:
                    angle = 90
            elif i > core[0]:
                if j < core[1]:  # 3rd quarter
                    angle = int(np.rad2deg(np.arctan(h/w))) + 180
                elif j > core[1]:  # 4th quarter
                    angle = int(np.rad2deg(np.arctan(w/h))) + 270
                else:
                    angle = 270
            else:
                angle = 0 if j > core[1] else 180

            feat[angle//bucketsize][t] += 1

    return np.array(feat)


def _extract_circular(minutae: np.array,
                      bucketsize: int):
    core = _get_core(minutae)
    if core is None:
        raise Exception('missing core point for circular method')

    dist = []
    for point in minutae:
        i, j, t, _ = point if len(point) == 4 else point + (None,)
        dist.append(np.linalg.norm(
            np.array((core[0], core[1])) - np.array((i, j))))

    feat = []
    for i in range(0, int(np.max(dist))//bucketsize + 1):
        feat.append({minucias.MnType.Termination: 0,
                     minucias.MnType.Bifurcation: 0})
    for i in range(0, len(dist)):
        t = minutae[i][2]
        if t == minucias.MnType.Termination or t == minucias.MnType.Bifurcation:
            feat[int(dist[i])//bucketsize][t] += 1

    return np.array(feat)


def extract(minutae: np.array,
            method: str = None,
            bucketsize: int = None):
    if method == 'radial':
        return (_extract_radial(minutae, bucketsize), method)
    elif method == 'circular':
        if bucketsize is None:
            raise Exception('bucketsize must be provided for circular method')
        return (_extract_circular(minutae, bucketsize), method)
    else:
        raise Exception(method + ' is not supported')


def distance(feat1: tuple,
             feat2: tuple):
    if feat1[1] != feat2[1]:
        raise Exception(feat1[1] + ' and ' + feat2[1] + ' methods not same!')

    d = 0
    if feat1[1] == 'radial':
        if len(feat1[0]) != len(feat2[0]):
            raise Exception('different block sizes for \'radial\' method are\
                not supported')
        for i in range(0, len(feat1[0])):
            f1 = np.array([feat1[0][i][minucias.MnType.Termination],
                           feat1[0][i][minucias.MnType.Bifurcation]])
            f2 = np.array([feat2[0][i][minucias.MnType.Termination],
                           feat2[0][i][minucias.MnType.Bifurcation]])
            d += np.linalg.norm(f1 - f2)
    if feat1[1] == 'circular':
        for i in range(0, np.max([len(feat1[0]), len(feat2[0])])):
            f1 = np.zeros(len(feat1[0][0]))
            if i < len(feat1[0]):
                f1 = np.array([feat1[0][i][minucias.MnType.Termination],
                               feat1[0][i][minucias.MnType.Bifurcation]])
            f2 = np.zeros(len(feat2[0][0]))
            if i < len(feat2[0]):
                f2 = np.array([feat2[0][i][minucias.MnType.Termination],
                               feat2[0][i][minucias.MnType.Bifurcation]])

            d += np.linalg.norm(f1 - f2)

    return d
