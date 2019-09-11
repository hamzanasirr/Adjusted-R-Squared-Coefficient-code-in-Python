def adjusted_r_squared(X, Y, r2):
    '''
    Returns a computed Adjusted R-Squared Coefficient.
    
    Parameters
    ----------
    X : Pandas DataFrame
        A pandas DataFrame including all the independant variables. Could be a series if there is only one predictor.
        
    Y : Pandas DataFrame or Series
        Labels or response variables 'Y'.
        
    r2 : float
        R-Squared Coefficient
    '''
    n = len(Y)
    p = X.shape[1]
    adj_r = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

    return adj_r