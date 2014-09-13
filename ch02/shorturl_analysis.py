# -*- coding: utf-8 -*-
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

    return time_zones

if __name__ == '__main__':
    print main()
