# -*- coding: utf-8 -*-
from collections import defaultdict
import json
import os

def main():
    """

    """
    datadir = os.path.dirname(os.path.abspath(__file__)) + '/../pydata-book/'
    path = datadir + '/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    with open(path) as f:
        records = [json.loads(line) for line in f]

    time_zones = [r['tz'] for r in records if 'tz' in r]

    tz_counts = get_counts(time_zones)

    return top_counts(tz_counts)

def get_counts(sequence):
    counts = defaultdict(int) # values initialize to zero
    for x in sequence:
        counts[x] += 1

    return counts

def top_counts(count_dict, n=10):
    """
    :type count_dict: dict
    :type n: int
    """
    counts = [(count, tz) for tz, count in count_dict.items()]
    counts.sort()

    return counts[-n:]

if __name__ == '__main__':
    print main()
