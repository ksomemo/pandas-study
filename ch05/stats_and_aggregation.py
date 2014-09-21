# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas.io.data

def main():
    """
    Calculation and aggregation of summary statistics
    """

    # Summary of statistics
    # return is not ndarray
    df = DataFrame([[1.4, np.nan],
                    [7.1, -4.5],
                    [np.nan, np.nan],
                    [0.75, -1.3]],
                   index=list('abcd'),
                   columns=['one', 'two'])
    print df
    print df.sum()
    print df.sum(axis=1)
    print df.mean(axis=1) # exclude nan
    print df.mean(axis=1, skipna=False)
    print df.idxmin()
    print df.idxmax()
    print df.cumsum()
    print df.describe()
    # values are not number
    obj = Series(list('aabc') * 4)
    print obj.describe()


    methods = ['count', 'min', 'max', # 'argmin', 'argmax',
               'quantile', 'median', 'mad', 'var', 'std',
               'skew', 'kurt', 'cummin', 'cummax', 'cumprod',
               'diff', 'pct_change']

    for method in methods:
        print u'「{0}」'.format(method)
        print getattr(df, method)()
        print ''

    # Correspond and Covariance
    all_data = {}
    lst = [] # ['AAPL', 'IBM', 'MSFT'] #, 'GOOG']:
    for ticket in lst: #, 'GOOG']:
        # IOError: after 3 tries, Yahoo! did not return a 200
        # for url 'http://ichart.finance.yahoo.com/table.csv?s=GOOG&a=0&b=1&c=2000&d=0&e=1&f=2010&g=d&ignore=.csv'
        all_data[ticket] = pd.io.data.get_data_yahoo(ticket, '1/1/2000', '1/1/2010')
    price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
    volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
    if all_data:
        returns = price.pct_change()
        print returns.tail()
        print ''
        print returns.MSFT.corr(returns.IBM)
        print returns.MSFT.cov(returns.IBM)
        print ''
        print returns.corr()
        print returns.cov()
        print ''
        print returns.corrwith(returns.IBM)
        print returns.corrwith(volume)

    # unique, frequency, belong
    print '',''
    obj = Series(list('cadaabbcc'))
    uniques = obj.unique()
    print uniques
    print obj.value_counts()
    print pd.value_counts(obj.values, sort=False)
    mask = obj.isin(['b', 'c'])
    print mask
    print obj[mask]

    data = DataFrame({
        'Qu1' : [1,3,4,3,4],
        'Qu2' : [2,3,1,2,3],
        'Qu3' : [1,5,2,4,4],
    })
    print data
    print data.apply(pd.value_counts).fillna(0)


if __name__ == '__main__':
    main()