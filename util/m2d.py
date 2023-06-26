# import mistune
# from mistune import preprocessing
import pandas as pd

from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
options = Namespace()
parser.add_argument('input_file', nargs='*',
                    help='files to convert to reST format')

# def convert(text, **kwargs):
#     return M2R(**kwargs)(text)


# def parse_from_file(file, encoding='utf-8', **kwargs):
#     if not os.path.exists(file):
#         raise OSError('No such file exists: {}'.format(file))
#     with open(file, encoding=encoding) as f:
#         src = f.read()
#     output = convert(src, **kwargs)
#     return output

def parse_options():
    parser.parse_known_args(namespace=options)

# class md(mistune.Markdown):
    
#     def __init__(self):
#         # print('init')
#         super(md, self).__init__()

#     # def parse(self, text):
#     #     print('new parse', text)
#     #     out = self.output(preprocessing(text))

#     #     return out
    
#     def output(self, text, rules=None):
#         self.tokens = self.block(text, rules)
#         # self.tokens.reverse()

#         # self.inline.setup(self.block.def_links, self.block.def_footnotes)

#         # print(self.tokens)
#         # out = self.renderer.placeholder()
#         # while self.pop():
#         #     out += self.tok()
#         # return out
#         # print('new output', self.tokens)
#         out = ""

#         while self.pop():
#             out += self.tok()
#         # return self.tokens
#         return out

class m2d:

    def __init__(self, **kwargs):

        # print(kwargs)
        self.log_md = './docs/changelog.md'
        self.summary_md = './docs/chg_summary.md'
        self.pkl_nm = './docs/changelog.pickle'

        self._inx = 0
        self._pre_h = ''
        self._new_h = ''
        self._content = ''
        self._df = pd.DataFrame(columns=['seq', 'title', 'content'], dtype='str')
        self._file = kwargs['file'] if kwargs else self.log_md
        # print(self._file)

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
        # print(self._inx)
        if self._inx != 0:
            self._df.loc[self._df.shape[0]] = [
                self._inx,
                self._pre_h,
                self._content
            ]
        # print(self._df.head())

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
            # print(text)

        self.update()
        self.save_pickle()
        # print(self._df.head())
        f.close()

    def write_md(self):
        f = open(self.summary_md, 'w', encoding='utf-8')

        self.read_pickle()

        for i, row in self._df.head(4).iterrows():
            # print(i[1][0])
            f.writelines([str(row[1]), str(row[2])])
        f.close()

def main():
    # mistune.Markdown()

    parser.parse_known_args(namespace=options)

    # dt = m2d(file='./docs/changelog.md')
    dt = m2d()
    dt.create()
    dt.write_md()

    # print(dt._df.head())
    # result = mistune.markdown(options.input_file[0], escape=True, renderer='ast', plugins=None)
    # result = mistune.markdown(text, escape=True, renderer='ast', plugins=None)
    # result = mistune.markdown(text, escape=True, renderer=None, plugins=None, temp='ast')
    # mk = mistune.Markdown()
    # mk = md()
    # result, _ = mk.parse(text)
    # # token = mk.token
    # print(result[0]['type'])
    # for file in options.input_file:
    #     output = parse_from_file(file)
    #     if options.dry_run:
    #         print(output)
    #     else:
    #         save_to_file(file, output)

if __name__ == '__main__':
    main()