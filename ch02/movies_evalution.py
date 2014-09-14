# -*- coding: utf-8 -*-

import pandas as pd
import study

def main():
    metadata = {
        'users': {
            'names': ['user_id', 'gender', 'age', 'occupation', 'zip'],
            'dat': 'users.dat'
        },
        'ratings': {
            'names': ['user_id', 'movie_id', 'rating', 'timestamp'],
            'dat': 'ratings.dat'
        },
        'movies': {
            'names': ['movie_id', 'title', 'genre'],
            'dat': 'movies.dat'
        }
    }

    # data loading
    tables = {}
    for k, v in metadata.items():
       tables[k] = read_table(study.DATA_DIR + 'ch02/movielens/' + v['dat'], v['names'])
    # join(ratings.user_id = users.user_id, ratings.movie_id = movies.movie_id)
    data = pd.merge(pd.merge(tables['ratings'], tables['users']), tables['movies'])

    # u'タイトル別評価件数のうち、件数が上位である映画に対する女性の平均評価
    mean_ratings = data.pivot_table(
        'rating', rows='title', cols='gender', aggfunc='mean'
    )
    ratings_by_title = data.groupby('title').size()
    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    mean_ratings = mean_ratings.ix[active_titles]
    top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
    print top_female_ratings['F'][:10]

    # calculate for each row
    mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
    sorted_by_diff = mean_ratings.sort_index(by='diff')
    print sorted_by_diff[:15]

    # u'評価の別れた映画TOP10
    ratings_std_by_title = data.groupby('title')['rating'].std()
    ratings_std_by_title = ratings_std_by_title.ix[active_titles]
    print ratings_std_by_title.order(ascending=False)[:10]

def read_table(file_path, names, sep='::', header=None):
    return pd.read_table(file_path, sep=sep, header=header, names=names)

if __name__ == '__main__':
    print main()
