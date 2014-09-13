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

    return {
        'new_york_cnt': tz_counts['America/New_York'],
        'total': len(time_zones),
        'city_cnt': len(tz_counts),
    }

def get_counts(sequence):
    counts = defaultdict(int) # values initialize to zero
    for x in sequence:
        counts[x] += 1

    return counts

if __name__ == '__main__':
    print main()
