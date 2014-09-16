# -*- coding: utf-8 -*-
import os
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Vector operation
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)

    print points
    print xs
    print ys

    x, y = np.meshgrid(np.array([1,2,3]), np.array([4,5,6,7]))
    print x # 4 rows, row is [1,2,3]
    print y # 4 rows, each row[0] is 4,5,6,7. columns are all same.
    # Missing ** in book
    z = np.sqrt(xs ** 2 + ys ** 2)
    print z
    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()
    # $...$ is √(x^2 + y^2)
    print "$\sqrt{x^2 + y^2}$ displayed as it is"
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    plt.show()

    # Representation of the ndarray of condition control
    print ''; print '' # multi statement
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = xarr.copy() + 1
    cond = np.array([True, False, True, True, False])
    # 1.4 displayed as 1.3999999999999.
    print [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
    # 1.4 displayed as 1.4.
    print np.where(cond, xarr, yarr)
    # create ndarray(bool), map to constant when value is true.
    print np.where(xarr >= 1.3, 2, yarr)

    # Math, Statistics
    print '\n'
    arr = np.arange(20)[::-1].reshape(5, 4)
    print arr
    print arr.mean(), np.mean(arr) # same
    print arr.sum(), np.sum(arr) # same
    print arr.mean(axis=1) # mean of the rows
    print arr.mean(axis=0) # mean of the columns
    print arr.sum(0) # sum of the columns
    print arr.sum(1) # sum of the rows
    print arr.argmin(), arr.argmax()
    print arr.argmin(1), arr.argmax(0)

    arr = np.arange(9).reshape(3, 3)
    print arr
    print arr.cumsum(0)
    print arr.cumprod(1) # u'累積積

    # boolean
    print '', ''
    bools = np.array([False, False, True, False])
    print bools
    print bools.any()
    print bools.all()

    # sort
    print '', ''
    arr = np.arange(9)[::-1]
    print arr
    print np.sort(arr)
    print arr # not sorted
    arr.sort()
    print arr # sorted
    arr = arr[::-1].reshape(3, 3)
    print arr
    print np.sort(arr, 1)
    print np.sort(arr, 0)

    # Set function
    print '',''
    names = ['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']
    # sorted(set(names))
    print np.unique(names) # ndarray.uniq() not found, sorted
    print sorted(set(names)) # same
    # if each name in list
    print np.in1d(names, ['Bob', 'Will'])
    xs, ys = (np.array([1,2,3]), np.array([2,3,4]))
    print np.intersect1d(xs, ys)
    print np.setdiff1d(xs, ys)
    print np.setxor1d(xs, ys)
    print np.union1d(xs, ys)

    # input/output(binary, text, memory)
    # binary
    print '',''
    pwd = os.path.abspath(os.path.dirname(__file__))
    arr = np.arange(10)
    np.save(pwd + '/some_array', arr)
    print np.load(pwd + '/some_array.npy')
    np.savez(pwd + '/array_archive.npz', a=arr, b=arr[::-1])
    arch = np.load(pwd + '/array_archive.npz')
    print arch
    print arch['b']

    # text
    print '',''
    file_name = pwd + '/array_ex.txt'
    if not os.path.exists(file_name):
        f = file(file_name, 'w')
        content ="""0,1,2
3,4,5
6,7,8
"""
        f.write(content)
        f.close()
    print np.loadtxt(file_name, delimiter=',')

    # Matrix calculation
    print '',''
    x = np.array([[1,2,3],[4,5,6]])
    y = np.array([[6,23],[-1,7],[8,9]])
    ones = np.ones(3)
    sq_mat = np.array([[1,2],[3,4]]) # Square matrix
    print x
    print y
    print ones
    print x.dot(y) # u'内積
    print x.dot(ones)
    print x.T # u'転置行列
    # u'線形代数:Linear Algebra
    print np.linalg.inv(sq_mat) # u'逆行列, 正方行列に対して計算する
    print np.linalg.qr(x) # u'QR分解
    print np.linalg.det(sq_mat) # u'行列式
    print np.linalg.eig(sq_mat) # u'固有値と固有ベクトル

    # Random number
    print '',''
    samples = np.random.normal(size=(4,4))
    print samples

    ex_random_timeit="""
import random
import numpy as np
N = 1000000
%timeit samples = [random.normalvariate(0,1) for _ in xrange(N)]
# 1 loops, best of 3: 1.52 s per loop
%timeit np.random.normal(size=N)
# 10 loops, best of 3: 42.7 ms per loop
"""

    print [np.random.randint(1,6) for _ in range(10)]
    # other functions
    # u'二項分布、正規分布、ベータ分布、カイ二乗分布、ガンマ分布、[0,1)の一様分布など

    # Random walk
    print '',''
    position = 0
    walk = [position]
    steps = 1000
    for i in xrange(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)
    ax = plt.figure().gca()
    ax.plot(walk)
    plt.show()

    nsteps = 1000
    draws = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    print walk.min(), walk.max()
    ax = plt.figure().gca()
    ax.plot(walk)
    plt.show()
    print (np.abs(walk) >= 10).argmax() # u'最初に±10の地点に到達したstep

    nwalks = 5000
    nsteps = 1000
    draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # more 0, less than 2(=1)
    steps = np.where(draws > 0, 1, -1)
    walks = steps.cumsum(1)
    print walks
    print walk.min(), walk.max()
    hits30 = (np.abs(walks) >= 30).any(1)
    print hits30
    print hits30.sum()

    crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
    print crossing_times.mean()

if __name__ == '__main__':
    main()
