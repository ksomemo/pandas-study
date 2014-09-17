# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import copy
import numpy as np
import sys


def main():
    # Series
    # Series is likea 1d array.
    lst = [4, 7, -5, 3]
    obj = Series(lst)
    print obj
    print obj.values
    print obj.index

    obj2 = Series(copy.deepcopy(lst), index=['d', 'b', 'a', 'c'])
    print obj2
    print obj2.index
    # numpy ndarray like
    print obj2['a']
    obj2['d'] = 6
    print obj2[['c', 'a', 'd']]
    print obj2
    print obj2[obj2 > 0]
    print obj2 * 2
    print np.exp(obj2)

    # dict like
    print 'b' in obj2, 'e' in obj2
    # dict to Series
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000,}
    obj3 = Series(sdata)
    print obj3

    # Value is NaN, if index not found.
    states = ['Calfornia', 'Ohio', 'Oregon', 'Texas']
    obj4 = Series(sdata, index=states)
    print obj4
    # Pandas function
    print pd.isnull(obj4)
    print pd.notnull(obj4)
    # Series method
    print obj4.isnull()

    # Value is NaN, Index that does not exist only on one side
    print obj3
    print obj4
    print obj3 + obj4

    # Index name
    obj4.name = 'population'
    obj4.index.name = 'state'
    print obj4

    # Change index
    obj4.index = ['a', 'b', 'c', 'd']
    print obj4

    # DataFrame
    # DataFrame is like a spread sheet(table)
    # DataFrame of Pandas are similar to R DataFrame
    print '',''
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9],}
    frame = DataFrame(data)
    print frame

    # Order columns
    print DataFrame(data, columns=['year', 'state', 'pop'])

    # Columns, named indexes
    # Column all value is NaN, if column not found in data
    frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                       index=['one', 'two', 'three', 'four', 'five'])
    print frame2
    print frame2.columns
    print frame2['state']
    print frame2.year
    # row data
    print frame2.ix['three']
    # Change column value
    frame2['debt'] = 16.5
    print frame2.debt
    frame2.debt = np.arange(5.) # error, size is not 5
    print frame2.debt

    # Column value is Nan, if index not found
    val = Series([-1.2, -1.5, -1.7], index=['one', 'three', 'five'])
    frame2.debt = val
    print frame2

    # new column. No frame.eastern
    frame2['eastern'] = frame2.state == 'Ohio'
    print frame2
    # del column. No frame.eastern
    del frame2['eastern']
    print frame2

    # nested dict to DataFrame
    # outer key is column, and sorted
    # inner key in index, and sorted
    pop = {'Ohio':{2002: 3.6, 2000: 1.5, 2001:1.7},
            'Nevada': {2001: 2.4, 2002:2.9},}
    frame3 = DataFrame(pop)
    print frame3
    # transpose
    print frame3.T
    # DataFrame is not sorted, if specify index/columns
    print DataFrame(pop, index=[2001, 2002, 2000], columns=['Ohio', 'Nevada'])

    # Values method return ndarray, ndarray has one type
    # return casted type, if ndarray has many type.
    print frame3.values
    print frame3.values.dtype
    print frame2.values
    print frame2.values.dtype
    print frame2['year'].values.dtype

    # Index Object(IntIndex, DateTimeIndex, PeriodIndex)
    obj = Series(range(3), index='a b c'.split(' '))
    index = obj.index
    print type(index)
    print index.dtype
    # Index is immutable
    try:
        index[1] = 'd'
    except:
        print sys.exc_info()

    print obj.index is pd.Index(['a', 'b', 'c'])
    index = pd.Index(np.arange(3))
    obj2 = Series(range(3), index=index)
    print obj2.index is index

    # Index as a Set
    print frame3
    print type(frame3.columns)
    print 'Ohio' in frame3.columns
    print 2003 in frame3.index
    print index.append(pd.Index(['d']))
    print index # result is true, immutable
    # other method are diff, intersection, union, isin, delete, drop, insert, etc.

if __name__ == '__main__':
    main()
