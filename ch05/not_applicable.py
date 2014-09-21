# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def main():
    """
    Handling of not applicable values
    """

    string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
    print string_data
    print string_data.isnull()
    string_data[0] = None
    print string_data.isnull()
    print None is np.nan, None == np.nan # not same

    # Exclude N/A
    print '',''
    NA = np.nan
    data = Series([1, NA, 3.5, NA, 7])
    print data.dropna()
    print data[data.notnull()]

    data = DataFrame([
        [1., 6.5, 3.],
        [1., NA, NA],
        [NA, NA, NA],
        [NA, 6.5, 3.]
    ])
    cleaned = data.dropna() # row that all value is not NA
    print data
    print cleaned
    print data.dropna(how='all')
    data[4] = None
    print data.dropna(axis=1, how='all')
    print data.dropna(thresh=2) # non NA is more 2

    # Fill NA
    print '',''
    print data.fillna(0)
    print data.fillna({1: 0.5, 2: -1})
    _ = data.fillna(0, inplace=True)
    print data
    print '',''
    df = DataFrame(np.arange(18).reshape((6, 3)))
    df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
    print df
    print df.fillna(method='ffill')
    print df.fillna(method='ffill', limit=2)
    data = Series([1., NA, 3.5, NA, 7])
    print data.fillna(data.mean())


if __name__ == '__main__':
    main()