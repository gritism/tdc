import mistune
from mistune import preprocessing

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

class md(mistune.Markdown):
    
    def __init__(self):
        print('init')
        super(md, self).__init__()

    def __call__(self):
        self.parse2()

    def parse2(self, text):
        print('parse2', text)
        out = self.output(preprocessing(text))

        return out
    
    def output(self, text, rules=None):
        self.tokens = self.block(text, rules)
        # self.tokens.reverse()

        # self.inline.setup(self.block.def_links, self.block.def_footnotes)

        # print(self.tokens)
        # out = self.renderer.placeholder()
        # while self.pop():
        #     out += self.tok()
        # return out
        out = ""

        while self.pop():
            out += self.tok()
        # return self.tokens
        return out

def main():
    # mistune.Markdown()

    parser.parse_known_args(namespace=options)

    with open(options.input_file[0], encoding='utf-8') as f:
        text = f.read()

    # result = mistune.markdown(options.input_file[0], escape=True, renderer='ast', plugins=None)
    # result = mistune.markdown(text, escape=True, renderer='ast', plugins=None)
    # result = mistune.markdown(text, escape=True, renderer=None, plugins=None, temp='ast')
    # mk = mistune.Markdown()
    mk = md()
    result = mk.parse2(text)
    # token = mk.token
    print(result)
    # for file in options.input_file:
    #     output = parse_from_file(file)
    #     if options.dry_run:
    #         print(output)
    #     else:
    #         save_to_file(file, output)

if __name__ == '__main__':
    main()