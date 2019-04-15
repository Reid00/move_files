import pandas as pd
import numpy as np
import re


class ReadCsv:

    def __init__(self, path):
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

        pattern = re.compile(r'/aviation_airport/([^_]+)')
        new_sk = []
        for sk in df['SubjectKey']:
            match = re.search(pattern, sk)
            new_sk.append(re.sub(match.group(1), match.group(1).upper(), sk))
            # print(sk)
        df['new_sk'] = new_sk
        df.to_csv('airport_upper.csv', columns=['SatoriID', 'new_sk'], index=False, header=None)


if __name__ == '__main__':
    # text = ReadCsv('url.txt')
    # text.read_text()
    # text.read_text_by_pd()
    csv_reader = ReadCsv('airport.csv')
    csv_reader.read_csv()
