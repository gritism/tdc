import mistune
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

def main():
    # mistune.Markdown()

    parser.parse_known_args(namespace=options)

    print(options)
    with open(options.input_file[0], encoding='utf-8') as f:
        text = f.read()

    result = mistune.markdown(text, escape=True, renderer='ast', plugins=None)
    # result = mistune.markdown(text)
    print(result)
    # for file in options.input_file:
    #     output = parse_from_file(file)
    #     if options.dry_run:
    #         print(output)
    #     else:
    #         save_to_file(file, output)

if __name__ == '__main__':
    main()