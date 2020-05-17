import pandas as pd
import numpy as np
import random

def gendat_ts():
    """Generates a synthetic time series dataset.

    """
    A = pd.DataFrame(pd.date_range('2015-01-01', periods=100, freq='M', name='date'))
    B = pd.DataFrame([random.gauss(mu=0, sigma=1) / 100 for _ in range(100)], columns=['val'])
    Z = pd.concat([A, B], axis=1)
    Z['cum_val'] = Z['val'].cumsum()
    return Z
