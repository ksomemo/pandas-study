# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from pandas.util.testing import MultiIndex


def main():
    """
    Handling of not applicable values
    """

    data = Series(np.random.randn(10),
                  index=[list('aaabbbccdd'), map(int, list('1231231223'))])
    print data
    print data.index
    print type(data.index)

    print data['b']
    print data['b':'c']
    print data.ix[['b', 'd']]
    print data[:, 2]

    print data.unstack()
    print data.unstack().stack()

    print '',''
    frame = DataFrame(np.arange(12).reshape((4, 3)),
                      index=[['a','a','b','b'], [1,2,1,2]],
                      columns=[['Ohio', 'Ohio', 'Colorado'],
                               ['Green', 'Red', 'Green']])
    print frame
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print frame

    print frame['Ohio']
    print MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                                 names=['state', 'color'])

    # change hierarchy and sort
    print '',''
    print frame.swaplevel('key1', 'key2')
    print '',''
    print frame.sortlevel(1) # sorted by key2
    print '',''
    print frame.swaplevel(0, 1).sortlevel(0) # swap and sorted by key 2

    # summary statistics for each hierarchy
    print '',''
    print frame.sum(level='key2')
    print '',''
    print frame.sum(level='color', axis=1)
    print '',''

    # Using column of the DataFrame for index
    print '','-------------------------'
    frame = DataFrame({
        'a': range(7),
        'b': range(7, 0, -1),
        'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
        'd': [0, 1, 2, 0, 1, 2, 3],
    })
    print frame
    frame2 = frame.set_index(['c', 'd'])
    print '',''
    print frame2
    print '',''
    print frame.set_index(['c', 'd'], drop=False)
    print '',''
    print frame2.reset_index()

if __name__ == '__main__':
    main()