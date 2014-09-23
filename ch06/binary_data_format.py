# -*- coding: utf-8 -*-
import os
import study
import pandas as pd
from study import p, cat

def main():
    """
    Binary data format
    """
    out_dir = os.path.dirname(__file__)

    ex1_path = study.DATA_DIR + '/ch06/ex1.csv'
    cat(ex1_path)
    frame = pd.read_csv(ex1_path)
    p(frame)

    out_pickle = out_dir + '/frame_pickle'
    # deprecated
    # frame.save(out_pickle)
    # pd.load(out_pickle)
    frame.to_pickle(out_pickle)
    p(pd.read_pickle(out_pickle))

    p('6.2.1 Hierarchical Data Format(HDF)----------------')
    h5_path = out_dir + '/mydata.h5'
    store = pd.HDFStore(h5_path)
    store['obj1'] = frame
    store['obj_col1'] = frame['a']
    p(store)
    p(store.obj1)

    p('6.2.2 Excel-------------------')
    xls_file = pd.ExcelFile(out_dir + '/data.xlsx')
    table = xls_file.parse('Sheet1')
    p(table)

if __name__ == '__main__':
    main()