def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    i = 0
    count = 0
    n = len(points)
    k = len(bins)
    res = [0.0] * k

    for p in points:
        # condition here
        while (i < k and p >= bins[i][1]):
            left, right = bins[i]
            res[i] = (count / (n * (right - left)))

            i += 1
            count = 0

        count+=1

    left, right = bins[i]
    res[i] = (count / (n * (right - left)))

    return res

    
            