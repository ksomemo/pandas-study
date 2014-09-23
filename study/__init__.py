import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../'
DATA_DIR = ROOT_DIR + '/pydata-book/'

def p(value):
    print '', ''
    print value

def cat(path):
   with open(path) as f:
        print ''
        for l in f.readlines(): print l,;
        print ''
