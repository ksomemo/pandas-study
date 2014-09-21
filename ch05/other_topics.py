# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

def main():

    ser = Series(np.arange(3.))
    ser2 = Series(np.arange(3.), index=list('abc'))
    print ser
    print ser2
    print '',''
    # print ser[-1]
    print ser2[-1]
    print '',''
    print ser.ix[:1]

    print '',''
    ser3 = Series(range(3), index=[-5, 1, 3])
    print ser3
    print '',''
    print ser3.iget_value(2)
    print '',''
    frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
    print frame
    print '',''
    print frame.irow(0)

    # panel
    # u'３次元のデータフレーム/パネルの各項目(列)はデータフレーム
    print '','----------------------'
    lst = ['AAPL', 'MSFT'] # , 'DELL', 'GOOG'
    pdata = pd.Panel(dict((stk, pd.io.data.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
                           for stk in lst))
    if not pdata.empty:
        print pdata
        pdata = pdata.swapaxes('items', 'minor')
        print '',''
        print pdata['Adj Close']
        print '',''
        print pdata.ix[:, '6/1/2012', :]
        print '',''
        print pdata.ix['Adj Close', '5/22/2012', :]
        print '', ''
        print type(pdata.ix[:, '5/30/2012', :]) # DataFrame
        if hasattr(pdata.ix[:, '5/30/2012', :], 'to_frame'):
            stacked = pdata.ix[:, '5/30/2012', :].to_frame()
            print stacked
            print '',''
            print stacked.to_panel()
        if hasattr(pdata, 'to_frame'):
            f1 = pdata.to_frame()
            print f1
            print '',''
            print f1.to_panel()
            print '',''

if __name__ == '__main__':
    main()