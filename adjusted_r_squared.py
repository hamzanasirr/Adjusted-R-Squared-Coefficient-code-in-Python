def adjusted_r_squared(X, Y, r2):
    n = len(Y)
    p = X.shape[1]
    adj_r = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

    return adj_r