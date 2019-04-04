import pandas as pd
import numpy as np


def read_txt():
    with open('urls.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split('\t')[0]
            # with open('res.txt', 'a', encoding='utf-8') as res:
            #     res.write(line + '\n')

    data = pd.read_csv('urls.txt', sep='\s+', header=None, encoding='utf-8', names=['url', 'num', 'data'])
    print(data)
    # data.to_csv('test.txt', columns=['url'], index=False, header=None)


if __name__ == '__main__':
    # read_txt()