# -*- coding: utf-8 -*-
from collections import defaultdict, Counter
import json
import os
from pandas import DataFrame


def main():
    """

    """
    datadir = os.path.dirname(os.path.abspath(__file__)) + '/../pydata-book/'
    path = datadir + '/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
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

    return tz_counts[:10]

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

if __name__ == '__main__':
    print main()
