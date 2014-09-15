# -*- coding: utf-8 -*-
import numpy as np

def main():
    """

    """
    data1 = [6, 7.5, 8, 0, 1]
    data2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    arr1 = np.array(data1)
    arr2 = np.array(data2)

    print arr1
    print arr2

    # dimension
    print arr2.ndim
    print arr2.shape

    # value type/specify type/cast
    print arr1.dtype
    print arr2.dtype
    print np.array(data1, dtype=np.int32).dtype
    print np.array(data2).astype(np.float32).dtype

    # values are zero.
    print np.zeros((3, 6))
    # values are random.
    print np.empty((2, 3, 2))
    # all values are one.
    print np.ones((2, 3))
    # range like
    print np.arange(15)
    # identity matrix
    print np.eye(2)
    print np.identity(3)

    # calculation
    print arr1 + arr1
    print arr1 - arr1
    print arr1 * 3
    print arr1 ** 2
    print 1 / arr1 # 0 div => inf
    print 1 / arr2

    print_headline('slice')
    print arr1[1]
    part = arr1[1:3]
    print part
    part[0:2] = 99.9 # broadcast
    print part
    print arr1 # reference
    copy = arr1[1:3].copy()
    copy[0:2] = 100.0
    print arr1

    print_headline('multi dimension operation')
    print arr2[1]
    print arr2[1][2]
    print arr2[1, 2]
    print arr2[:1, :2]

    print_headline('bool index reference')
    names = np.array(
        ['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']
    )
    data = np.random.randn(7, 4)
    print names
    print data
    # each value bool
    print names == 'Bob' # True are 0 and 3
    print data[names == 'Bob'] # display only Row 0 and 3
    print names != 'Bob' # Other
    print -(names == 'Bob') # same not equal
    print (names == 'Bob') | (names == 'Will') # can't use or
    print (names == 'Bob') & (names == 'Will') # can't use and
    # compare
    data[data < 0] = 0.0
    print data

    print_headline('use integer array index reference')
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print arr
    # specify row index list
    print arr[[4, 3, 0, 6]]
    print arr[[-3, -5, -7]]
    # arr.shape => (8, 4)
    arr = np.arange(32).reshape((8, 4))
    print arr
    # [arr[1, 0],arr[5, 3],arr[7, 1],arr[2, 2]]
    print arr[[1, 5, 7, 2], [0, 3, 1, 2]]
    # u' 対象行に対して、全ての行をそのまま受け取り、列を入れ替える
    print arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
    print arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]

    print_headline('identity matrix and transpose columns and rows')
    arr = np.arange(15).reshape((3, 5))
    print arr
    print arr.T
    print np.dot(arr.T, arr)
    arr = np.arange(16).reshape((2, 2, 4))
    print arr
    print arr.transpose((1, 0, 2))
    print arr.swapaxes(1, 2)

def print_headline(title):
    print ''
    print '-----{0}--------'.format(title)
    print ''

if __name__ == '__main__':
    print main()
