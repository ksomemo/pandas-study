# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

def main():
    # reindex
    obj = Series(range(4), index='a b c d'.split(' ')[::-1])
    print obj

    obj2 = obj.reindex('a b c d e'.split(' '))
    print obj2

    # Change NaN
    print obj.reindex('a b c d e'.split(' '), fill_value=0)
    colors = ['blue', 'purple', 'yellow']
    index = [0,2,4]
    obj3 = Series(colors, index=index)
    print obj3.reindex(range(6))
    print obj3.reindex(range(6), method='ffill') # not found forward fill
    print obj3.reindex(range(6), method='backfill') # bfill

    # DataFrame
    states = ['Ohio', 'Texas', 'California']
    frame = DataFrame(np.arange(9).reshape((3,3)),
                    index='a b c'.split(' '),
                    columns=['Ohio', 'Texas', 'California'])
    print frame
    frame2 = frame.reindex('a b c d'.split(' '))
    print frame2
    states[0] = 'Utah'
    states[1], states[0] = states[:2]
    print frame.reindex(columns=states)
    # fill
    print frame.reindex('a b c d'.split(' '), method='ffill', columns=states)
    print frame.ix['a b c d'.split(' ')]
    print frame.ix['a b c d'.split(' '), states]

    # Delete column
    print '',''
    obj = Series(range(5), index='a b c d e'.split(' '))
    new_obj = obj.drop('c')
    print new_obj
    print obj

    # Index reference
    print '',''
    obj = Series(np.arange(4.), index='a b c d'.split(' '))
    print obj['b']
    print obj[1] # same
    print obj[2:4]
    print obj[['b', 'a', 'c']]
    print obj[[1,3]]
    print obj[obj < 2]
    # Slice with label
    print obj['b':'c'] # include 'c'
    obj['b':'c'] = 5
    print obj


    data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    print data
    # column
    print data['two']
    print data[['three', 'one']]
    # row
    print data[:2]
    print data[data['three'] > 5]
    # all values
    print data < 5
    data[data < 5] = 0
    print data
    # row and column
    print data.ix[['Colorado'], ['two', 'three']]
    print data.ix[['Colorado', 'Utah'], [3, 0, 1]]
    # row
    print data.ix[2]
    # label row and column, return column
    print data.ix[:'Utah', 'two']
    # xs
    # row
    print data.xs('Utah')
    print data.xs('Utah', axis=0)
    # rows
    print data.xs('two', axis=1)
    # icol/irow i is index
    print data.icol(1)
    print data.irow(1)

    # Union
    print '',''
    s1 = Series([7.3, -2.5, 3.4, 1.5],          index=['a', 'c', 'd', 'e'])
    s2 = Series([-2.1, 3.6,      -1.5, 4, 3.1], index=['a', 'c',      'e', 'f', 'g'])
    print s1
    print s2
    # index is union, but d, f, g are NaN
    print s1 + s2
    df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                    index=['Ohio', 'Texas', 'Colorado'])
    df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print df1
    print df2
    print df1 + df2

    # arithmetic method
    print '',''
    df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
    df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
    print df1
    print df2
    print df1.add(df2, fill_value=0)
    # reindex has fill_value argument
    # other arithmetic method are sub/div/mul(ti)

    # Calculation in a DataFrame and Series
    print '',''
    # subtract from each row. broadcat
    arr = np.arange(12.).reshape((3, 4))
    print arr
    print arr[0]
    print arr - arr[0]
    frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    series = frame.ix[0]
    print frame
    print series
    print frame - series

    series2 = Series(range(3), index=list('bef'))
    print frame + series2

    series3 = frame['d']
    series4 = frame.ix[0]
    print frame
    print series3
    print series4
    print frame.sub(series3, axis=0)
    print frame.sub(series4, axis=1)

    # apply function and mapping
    print '', ''
    frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print frame
    f = lambda x: x.max() - x.min()
    print frame.apply(f)
    print frame.apply(f, axis=1)

    f = lambda x: Series([x.min(), x.max()], index=['min', 'max'])
    print frame.apply(f)

    format = lambda x: '{0:.2f}'.format(x)
    print frame.applymap(format) # frame
    print frame['e'].map(format) # series

    # sort and rank
    print '',''
    obj = Series(range(4), index=list('dabc'))
    print obj
    print obj.sort_index()

    frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                      columns=list('dabc'))
    print frame
    print frame.sort_index()
    print frame.sort_index(axis=1)
    print frame.sort_index(axis=1, ascending=False)

    # Sorting series
    print '',''
    obj = Series([4, 7, -3, 2])
    print obj.order()
    obj = Series([4, np.nan, 7, np.nan, -3, 2])
    print obj.order()
    print obj.order(ascending=False)

    # order by multi columns
    print '',''
    frame = DataFrame({
        'b': [4, 7, -3, 2],
        'a': [0, 1, 0, 1],
    })
    print frame.sort_index(by=['a', 'b'])

    # rank
    print '',''
    obj = Series([7, -5, 7, 4, 2, 0, 4])
    print obj.rank() # method is average
    print obj.rank(method='first') # No Duplicates
    print obj.rank(ascending=False, method='min')
    print obj.rank(ascending=False, method='max')
    f1 = DataFrame(obj, columns=['data'])
    f2 = DataFrame(obj.rank(), columns=['rank'])
    # merge by each index
    print pd.merge(f1, f2, left_index=True, right_index=True)

    # Index of the axis with duplicate values
    print '',''
    obj = Series(range(5), index=list('aaabc'))
    print obj
    print obj.index.is_unique
    print obj['a']
    print obj['c']

    df = DataFrame(np.arange(12.).reshape((4, 3)), index=list('aabb'),
                   columns=list('ccd'))
    print df
    print df.ix['b']
    print df['c']

if __name__ == '__main__':
    main()