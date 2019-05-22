import pandas as pd
import numpy as np
import re
import urllib.parse


class ReadCsv:
    def __init__(self, path=None):
        self.path = path

    def read_text(self):  # 读取csv或者txt，urls.txt 文件的第二列内容，用常规方法
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.split('\t')[0]
                with open('res.txt', 'a', encoding='utf-8') as res:
                    res.write(line + '\n')

    def read_text_by_pd(self):  # 读取csv或者txt 文件的第二列内容，用pandas
        data = pd.read_csv(self.path, sep='\s+', header=None, encoding='utf-8', names=['url', 'num', 'data'])
        print(data)
        data.to_csv('test_pd.txt', columns=['url'], index=False, header=None)

    def read_csv(self):  # 读取csv， 修改某一列或者某一个行的参数,airport.csv
        df = pd.read_csv(self.path, sep=',', header=0, encoding='utf-8')
        df1 = df.dropna()
        df1.to_csv('airport_dropna.csv', index=False, header=None)
        df2 = df.fillna(value=0)
        df2.to_csv('airport_fillna.csv', index=False, header=None)
        pattern = re.compile(r'/aviation_airport/([^_]+)')
        new_sk = []
        for sk in df['SubjectKey']:
            match = re.search(pattern, sk)
            new_sk.append(re.sub(match.group(1), match.group(1).upper(), sk))
            # print(sk)
        df['new_sk'] = new_sk
        df.to_csv('airport_upper.csv', columns=['SatoriID', 'new_sk'], index=False, header=None)

    def read_csv_by_chunk(self):  # 分块读取，写入csv某一列, need_check_urls.tsv
        chunksize = 40000
        reader = pd.read_csv(self.path, sep='\t', header=None, encoding='utf-8', chunksize=chunksize,
                             usecols=[2],
                             names=['urls'])
        i = 0
        for chunk in reader:
            url_decode = [urllib.parse.unquote(str(url)).strip('"') for url in chunk['urls']]
            chunk['url_decode'] = url_decode
            # chunk.shape[0] row number
            i = i + 1
            chunk.to_csv('./output/url_{}.tsv'.format(i), index=False, header=None, columns=['url_decode'])

    def compare_content(self, path1, path2):
        file_1 = pd.read_csv(path1, sep='\t', header=None, usecols=[0], names=['book_id'])
        file_2 = pd.read_csv(path2, sep='\t', header=None, usecols=[0], names=['book_id'])
        pattern = re.compile(r'(\d+)')
        file_1['id'] = [re.search(pattern, book_id).group(1).strip() for book_id in file_1['book_id']]
        file_2['id'] = [re.search(pattern, book_id).group(1).strip() for book_id in file_2['book_id']]
        # file_1.to_csv('./output/factbase.csv', index=False, header=None, columns=['id'])
        # file_2.to_csv('./output/view.csv', index=False, header=None, columns=['id'])
        df1 = pd.read_csv('./output/1.txt', sep='\t', names=['id', 'name', 'age'])
        df2 = pd.read_csv('./output/2.txt', sep='\t', names=['id', 'name'])
        # print([df1['id'] > 0])  # suggest use this method to get columns
        # print([df1.id > 0])  # not suggest get the column
        # print(df1[df1['id'] > 0])  # use this method filter some data
        # print(df1[df1['id'] > 0][['name', 'age']])  # use this method filter columns
        # print(df1[df1['id'] > 0]['name', 'age'])  # this method is wrong
        df4 = df1[~df1['id'].isin(df2['id'])]  # filter column  is not exsit in another DataFrame
        df5 = df1[df1['id'].isin(df2['id'])]  # filter column  exsit in another DataFrame
        df4.to_csv('./output/not_in.csv', index=False, header=True, columns=['id'])
        df5.to_csv('./output/in.csv', index=False, header=True, columns=['id'])
        df3 = pd.merge(df1, df2, how='outer', on='id')
        df3.to_csv('./output/outer_join.csv', index=False, header=True, )
        not_in_1 = df3.drop(df1.index)
        # print('not in \n', not_in_1)
        not_in_1.to_csv('./output/not_in_1.csv', index=False, header=True, columns=['id', 'name_x', 'name_y'])


if __name__ == '__main__':
    # text = ReadCsv('url.txt')
    # text.read_text()
    # text.read_text_by_pd()
    csv_reader = ReadCsv('airport.csv')
    csv_reader.compare_content(r'D:\v-baoz\python\dirs_files\input\urls_from_fact_base.tsv',
                               r'D:\v-baoz\python\dirs_files\input\urls_from_view.tsv')
