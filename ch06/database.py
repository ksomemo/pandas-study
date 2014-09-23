# -*- coding: utf-8 -*-
import os
import sqlite3
from datetime import date, datetime, time
import traceback
import pymongo
import study
import pandas.io.sql as sql
from pandas import DataFrame
from study import p, cat

def main():
    """
    Binary data format
    """
    out_dir = os.path.dirname(__file__)

    query = """
CREATE TABLE test
(
    a VARCHAR(20)
    , b VARCHAR(20)
    , c REAL
    , INTEGER
);"""
    con = sqlite3.connect(out_dir + '/ch06-sqlite.db')
    try:
        con.execute(query)

        data = [('Atlanta', 'Georgia', 1.25, 6),
                ('Tallahassee', 'Florida', 2.6, 3),
                ('Sacramento', 'California', 1.7, 5)]
        stmt = 'INSERT INTO test VALUES(?, ?, ?, ?)'
        con.executemany(stmt, data)
        con.commit()
    except sqlite3.OperationalError as e:
        print e.message
        print traceback.format_exc()
    finally:
        p('finally')

    cursor = con.execute('select * from test')
    rows = cursor.fetchall()
    p(rows)
    p(cursor.description)
    p(DataFrame(rows, columns=zip(*cursor.description)[0]))
    p(sql.read_sql('select a, b, c from test', con))
    # deprecated
    # p(sql.read_frame('select a, b, c from test', con))
    con.close()

    p('6.4.1 MongoDB------------------')
    con = pymongo.Connection('localhost', port=27017)
    tweets = con.db.twees

    columns = ['created_at', 'from_user', 'id', 'text']
    date_combine = datetime.combine(date(2005, 7, 14), time(12, 30))
    data = [
        [date.today().isoformat(),                     'a', 1, 'aa'],
        [str(date.today()),                            'b', 2, 'bb'],
        [date.today().strftime('%Y-%m-%d %H:%M:%S'),   'c', 3, 'cc'],
        [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'd', 4, 'dd'],
        [date_combine.strftime('%Y-%m-%d %H:%M:%S'),   'd', 4, 'dd'],
    ]
    for d in data:
        r = dict(zip(columns, d))
        print r
        tweets.save(r)

    cursor = tweets.find({'from_user': 'd'})
    p(DataFrame(list(cursor), columns=columns))

if __name__ == '__main__':
    main()