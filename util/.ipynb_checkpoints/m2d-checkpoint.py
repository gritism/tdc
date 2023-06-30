import pandas as pd
from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
options = Namespace()
parser.add_argument('input_file', nargs='*',
                    help='files to convert to reST format')

def parse_options():
    parser.parse_known_args(namespace=options)

class m2d:

    def __init__(self, **kwargs):

        self.log_md = './docs/changelog.md'
        self.summary_md = './docs/chg_summary.md'
        self.pkl_nm = './docs/changelog.pickle'

        self._inx = 0
        self._pre_h = ''
        self._new_h = ''
        self._content = ''
        self._df = pd.DataFrame(columns=['seq', 'title', 'content'], dtype='str')
        self._file = kwargs['file'] if kwargs else self.log_md

    @property
    def inx(self):
        return self._inx

    def inc(self):
        self._inx += 1

    @property
    def pre_h(self):
        return self._pre_h

    @pre_h.setter
    def pre_h(self, s):
        self._pre_h = s

    @property
    def new_h(self):
        return self._new_h

    @new_h.setter
    def new_h(self, s: str):
        self._new_h = s
        self.update()
        self.initialize(s)
        self.inc()
        # print(self._new_h)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, s):
        self._content += s

    def initialize(self, s):
        self._pre_h = s
        self._content = ''

    def update(self):
        if self._inx != 0:
            self._df.loc[self._df.shape[0]] = [
                self._inx,
                self._pre_h,
                self._content
            ]

    def save_pickle(self):
        self._df.to_pickle(self.pkl_nm)

    def read_pickle(self):
        self._df = pd.read_pickle(self.pkl_nm)
        print(self._df.head())

    def create(self):
        f = open(self._file, 'r', encoding='utf-8')
        while f:
            text = f.readline()
            if not text: 
                break

            if text.startswith('#'):
                self._new_h = text
                self.update()
                self.initialize(text)
                self.inc()
            else:
                self._content += text

        self.update()
        self.save_pickle()
        f.close()

    def write_md(self):
        f = open(self.summary_md, 'w', encoding='utf-8')

        self.read_pickle()

        for i, row in self._df.head(4).iterrows():
            if i > 0:
                f.writelines([str(row[1]), str(row[2])])
        f.close()

def main():

    parser.parse_known_args(namespace=options)
    dt = m2d()
    dt.create()
    dt.write_md()

if __name__ == '__main__':
    main()
