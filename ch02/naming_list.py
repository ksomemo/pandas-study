# -*- coding: utf-8 -*-

import study
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    columns = ['name', 'sex', 'births']

    pieces = []
    years = range(1880, 2011)
    for year in years:
        path = '{0}/ch02/names/yob{1}.txt'.format(study.DATA_DIR, year)
        frame = pd.read_csv(path, names=columns)
        frame['year'] = year
        pieces.append(frame)
    # concat rows, delete index
    names = pd.concat(pieces, ignore_index=True)
    # cols is deprecated, use columns instead
    # rows is deprecated, use index instead
    total_births = names.pivot_table('births', index='year', columns='sex', aggfunc='sum')
    total_births.plot(title='Total births by sex and year')
    plt.show()

    # add prop
    groups = ['year', 'sex']
    names = names.groupby(groups).apply(add_prop)
    # verify sum is 1
    assert np.allclose(names.groupby(groups)['prop'].sum(), 1)

    # same for loop list.append => pd.concat
    grouped = names.groupby(groups)
    top1000 = grouped.apply(get_top1000)

    # u'男子・女子の名前の年代別推移の例
    # u'=>代表的な名前を付けなくなっている傾向があるのでは？という仮説をグラフから考えた
    total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc='sum')
    subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
    subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
    plt.show()

    # u'名前の種類の多様性の確認(上位が全体の中でどれくらいの割合であるか)
    table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc='sum')
    table.plot(title='Sum of table1000.prop by year and sex',
               yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
    plt.show()

    # u'年度ごとの名前の多様性変遷
    # u'結果として、1980年以降に多様となり、特に女子の名前が増えている
    diversity = top1000.groupby(groups).apply(get_quantile_count)
    diversity = diversity.unstack('sex')
    diversity.plot(title='Number of popular names in top 50%')
    plt.show()

    # u'名前の末尾文字の男女間の差異
    get_last_letter = lambda x: x[-1]
    last_letters = names.name.map(get_last_letter)
    last_letters.name = 'last_letter'
    table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc='sum')
    # Error>: CGContextClosePath: no current point, if you don't excluding NaN using fillna.
    subtable = table.reindex(columns=[1910, 1960, 2010], level='year').fillna(0.0)
    letter_prop = subtable / subtable.sum().astype(float)
    fix, axes = plt.subplots(2, 1, figsize=(10, 8))
    letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
    letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
    plt.show()

    # u'上記で特に多かった男子の末尾文字について
    # u'T: 転置行列（transposed matrix）
    letter_prop = table / table.sum().astype(float)
    dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
    dny_ts.plot(style={'d':'-.', 'n': '-', 'y': ':'})
    plt.show()

    # u'男子名前から女子名前へ定着、とその逆
    all_names = top1000.name.unique()
    mask = np.array(['lesl' in x.lower() for x in all_names])
    lesley_like = all_names[mask]
    filtered = top1000[top1000.name.isin(lesley_like)]
    table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
    # u'sum of sex(columns), axis is '軸'. axis is year(index).
    table = table.div(table.sum(1), axis=0)
    table.plot(style={'M': 'k-', 'F': 'k--'})
    plt.show()

def add_prop(group):
    births = group['births'].astype(float)

    group['prop'] = births / births.sum()

    return group

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]

def get_quantile_count(group, q=0.5):
    """
    u'cumsum is cumulative sum. (累積和)
    u'上記が0.5、つまり半分を超えるIndexを見つけることで、数がすくなければ上位の構成比が大きい
    """
    group = group.sort_index(by='prop', ascending=False)

    return group.prop.cumsum().values.searchsorted(q) + 1 # index started zero

if __name__ == '__main__':
    print main()
