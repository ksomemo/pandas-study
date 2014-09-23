# -*- coding: utf-8 -*-
import StringIO
import csv
from email import header
import json
from lxml import objectify
import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import sys
from pandas.io.parsers import TextParser
import study
from study import p, cat
from lxml.html import parse
from urllib2 import urlopen

def main():
    out_dir = os.path.dirname(__file__)

    ex1_path = study.DATA_DIR + '/ch06/ex1.csv'
    cat(ex1_path)

    df = pd.read_csv(ex1_path)
    p(df)
    p(pd.read_table(ex1_path, sep=','))

    p('header less---------------------')
    ex2_path = study.DATA_DIR + '/ch06/ex2.csv'
    cat(ex2_path)
    names = ['a','b', 'c', 'd', 'message']
    p(pd.read_csv(ex2_path, header=None))
    p(pd.read_csv(ex2_path, names=names))
    p(pd.read_csv(ex2_path, names=names, index_col='message'))

    p('hierarchy index---------------------')
    mindex_path = study.DATA_DIR + '/ch06/csv_mindex.csv'
    cat(mindex_path)
    p(pd.read_csv(mindex_path, index_col=['key1', 'key2']))

    p('separate by regex-------------')
    ex3_path = study.DATA_DIR + '/ch06/ex3.csv'
    cat(ex3_path)
    p(pd.read_csv(ex3_path, sep='\s+'))

    p('skip rows-----------')
    ex4_path = study.DATA_DIR + '/ch06/ex4.csv'
    cat(ex4_path)
    p(pd.read_csv(ex4_path, skiprows=[0,2,3]))

    p('N/A------------------')
    ex5_path = study.DATA_DIR + '/ch06/ex5.csv'
    cat(ex5_path)
    result = pd.read_csv(ex5_path)
    p(result)
    p(pd.isnull(result))
    result = pd.read_csv(ex5_path, na_values=['NULL', '12']) # 12 is NA
    p(result)

    p('N/A dict------------------')
    sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
    p(sentinels)
    p(pd.read_csv(ex5_path, na_values=sentinels))

    p('6.1.1 read data chunk size---------------------')
    ex6_path = study.DATA_DIR + '/ch06/ex6.csv'
    p(pd.read_csv(ex6_path).count())
    p(pd.read_csv(ex6_path, nrows=5))
    chunker = pd.read_csv(ex6_path, chunksize=1000)
    p(chunker)
    tot = Series([])
    for piece in chunker:
        tot = tot.add(piece['key'].value_counts(), fill_value=0)
    tot.order(ascending=False)
    p(tot[:10])

    p('6.1.2 write---------------------')
    data = pd.read_csv(ex5_path)
    p(data)

    ex5_out_path = out_dir + '/ex5_out.csv'
    data.to_csv(ex5_out_path)
    cat(ex5_path)

    data.to_csv(sys.stdout, index=False, header=False)
    print ''
    data.to_csv(sys.stdout, index=False, cols=list('abc'))
    print ''

    p('Series--------------')
    tseries_out_path = out_dir + '/tseries_out.csv'
    dates = pd.date_range('1/1/2000', periods=7)
    ts = Series(np.arange(7), index=dates)
    ts.to_csv(tseries_out_path)
    cat(tseries_out_path)
    p(Series.from_csv(tseries_out_path, parse_dates=True))

    p('6.1.3 csv-------------------------')
    ex7_path = study.DATA_DIR + '/ch06/ex7.csv'
    cat(ex7_path)
    f = open(ex7_path)
    reader = csv.reader(f)
    for line in reader:
        print line
    lines = list(csv.reader(open(ex7_path)))
    header, values = lines[0], lines[1:]
    data_dict = {h: v for h,v in zip(header, zip(*values))}
    p(data_dict)

    my_data_out_path = out_dir + '/mydata.csv'
    with open(my_data_out_path, 'w') as fp:
        writer = csv.writer(fp, dialect=my_dialect)
        writer.writerow(('one', 'two', 'three'))
        writer.writerow(('1', '2', '3'))
        writer.writerow(('4', '5', '6'))
        writer.writerow(('7', '8', '9'))
    cat(my_data_out_path)

    p('6.1.4 JSON-------------------------')
    obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
             {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
    result = json.loads(obj)
    p(result)
    asjson = json.dumps(result)
    p(asjson)
    siblings = DataFrame(result['siblings'], columns=['name', 'age'])
    p(siblings)

    p('6.1.4 XML/HTML Web Scraping-------------------------')
    url = '' #'http://finance.yahoo.com/q/op?s=AAPL+Options'
    if not url is '':
        parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
        doc = parsed.getroot()
        p([lnk.get('href') for lnk in doc.findall('.//a')][-10:])

        tables = doc.findall('.//table')
        p(parse_options_data(tables[9])[:5])
        p(parse_options_data(tables[13])[:5])

    p('6.1.5 Read XML-------------------------')
    xml_path = out_dir + '/Performance_MNR.xml'
    xml_content ="""
<INDICATOR>
    <INDICATOR_SEQ>373889</INDICATOR_SEQ>
    <PARENT_SEQ></PARENT_SEQ>
    <AGENCY_NAME>MEtro-North Railroad</AGENCY_NAME>
    <INDICATOR_NAME>Escalator Availability</INDICATOR_NAME>
    <DESCRIPTION>Percent of the time that escalators are operational systemwide. The availability rate is based on physical observations performed the morning of regular business days only. This is a new indicator the agency began reporting in 2009.</DESCRIPTION>
    <PERIOD_YEAR>2011</PERIOD_YEAR>
    <PERIOD_MONTH>12</PERIOD_MONTH>
    <CATEGORY>Service Indicators</CATEGORY>
    <FREQUENCY>M</FREQUENCY>
    <DESIRED_CHANGE>U</DESIRED_CHANGE>
    <INDICATOR_UNIT>%</INDICATOR_UNIT>
    <DECIMAL_PLACES>1</DECIMAL_PLACES>
    <YTD_TARGET>97.00</YTD_TARGET>
    <YTD_ACTUAL></YTD_ACTUAL>
    <MONTHLY_TARGET>97.00</MONTHLY_TARGET>
    <MONTHLY_ACTUAL></MONTHLY_ACTUAL>
</INDICATOR>
"""
    if not os.path.exists(xml_path):
        with open(xml_path, 'w') as f:
            f.write(xml_content)
    parsed = objectify.parse(open(xml_path))
    root = parsed.getroot()
    data = []
    skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
                   'DESIRED_SEQ', 'DECIMAL_PLACES']
    p(dir(root))
    for elt in root: # .INDICATOR:
        el_data = {}
        for child in elt.getchildren():
            if child.tag in skip_fields:
                continue
            el_data[child.tag] = child.pyval
        data.append(el_data)
    perf = DataFrame(data)
    p(perf)

    tag = '<a href="http://google.com">Google</a>'
    root = objectify.parse(StringIO.StringIO(tag)).getroot()
    p(root)
    p(root.get('href'))
    p(root.text)

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_ALL

def _unpack(row, kind='td'):
    elts = row.findall('.//{0}'.format(kind))
    return [val.text_content() for val in elts]

def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]

    return TextParser(data, names=header).get_chunk()

if __name__ == '__main__':
    main()