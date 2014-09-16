# -*- coding: utf-8 -*-
import numpy as np

def main():
    """
    universal function(ufunc)
    Function that returns the result of the operation of each element.
    Arg is ndarray, returns a ndarray
    """
    arr = np.arange(10)

    print_headline('arg is ndarray')
    print 'integer'
    print np.sqrt(arr)
    print np.exp(arr)
    print np.square(arr)
    print np.log10(arr)

    print ''
    print 'float'
    arr = np.array([-2, -1.6, -1.4, 0, 1.4, 1.6, 2])
    print np.sign(arr)
    print np.ceil(arr)
    print np.floor(arr)
    print np.rint(arr) # round
    print np.sin(arr) # cos, tan, arcxxx
    print np.logical_not([arr >= 1]) # and, or, xor

    print ''
    print 'NaN, inf'
    nan_inf = np.array([0, 1, np.NaN, np.inf, -np.inf])
    print nan_inf
    print np.isnan(nan_inf)
    print np.isinf(nan_inf)

    print_headline('args are ndarray')
    x = np.arange(8)
    y = np.arange(8)[::-1]
    print x, y
    print np.add(x, y)
    print np.subtract(x, y)
    print np.multiply(x, y)
    print np.divide(x, y)
    print np.floor_divide(x, y)
    print np.power(x, y)
    print np.mod(x, y)
    print np.maximum(x, y)
    print np.minimum(x, y)
    print np.greater_equal(x, y)

    print_headline('returns are ndarray')
    arr = np.random.randn(10)
    # divide integer ndarray and float ndarray
    modf = np.modf(arr)
    print arr
    print modf[0]
    print modf[1]




def print_headline(title):
    print ''
    print '-----{0}--------'.format(title)
    print ''

if __name__ == '__main__':
    print main()
