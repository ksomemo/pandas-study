# -*- coding: utf-8 -*-
from collections import defaultdict, Counter
import json
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import numpy as np
import study

def main():
    """

    """
    path = study.DATA_DIR + 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    with open(path) as f:
        records = [json.loads(line) for line in f]

    time_zones = [r['tz'] for r in records if 'tz' in r]

    # u'pandasのデータフレームを使用
    frame = DataFrame(records)
    print list(frame.columns.values)

    # u'列にアクセスして、Noneを置き換える
    clean_tz = frame['tz'].fillna('Missing')
    # u' clean_tz == '' => each row index: bool(if values is '' then true)
    clean_tz[clean_tz == ''] = 'Unknown'
    # u'それぞれの数を集計し、TOP10を表示
    tz_counts = clean_tz.value_counts()

    plot(tz_counts[:10])

    # u'a colomun is user agent.
    results = Series([x.split()[0] for x in frame.a.dropna()])

    # IDEA can't complement method when you enter frame.a .
    cframe = frame[frame['a'].notnull()]
    # return is np.ndarray.
    operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

    # pandas.core.groupby.DataFrameGroupBy
    # cframe group by args (ex. (tz1, Windows), (tz1, Not Windows), (tz2, Windows), ...)
    by_tz_os = cframe.groupby(['tz', operating_system])
    # size => each group sum
    #
    # unstack => list to table?
    #            b c
    # a b 1 => a 1 2
    # a c 2    d 1 NaN (not exists)
    # d b 1
    #
    # fillna => NaN to arg (returned type is pandas.core.frame.DataFrame)
    agg_counts = by_tz_os.size().unstack().fillna(0)

    # sum of group by tz when sum arg is 1
    # sum of group by os when sum arg is 0
    # argsort, returns indexes after sorting order by asc
    indexer = agg_counts.sum(1).argsort()

    count_subset = agg_counts.take(indexer)[-10:]
    plot(count_subset)

    # u'合計１になるように正規化して、OS分布を見やすくしている
    normed_subset = count_subset.div(count_subset.sum(1), axis=0)
    plot(normed_subset)

def get_counts(sequence):
    counts = defaultdict(int) # values initialize to zero
    for x in sequence:
        counts[x] += 1

    return counts

def top_counts(count_dict, n=10):
    counts = [(count, tz) for tz, count in count_dict.items()]
    counts.sort()

    return counts[-n:]

def top_counts_by_counter(count_dict, n=10):
    return Counter(count_dict).most_common(n)

def plot(dataframe, stacked=True):
    dataframe.plot(kind='barh', rot=0, stacked=stacked)
    # u' if don't use show, output is Out[9]: <matplotlib.axes.AxesSubplot at 0x108b94d10>
    plt.show()

if __name__ == '__main__':
    print main()
