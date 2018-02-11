import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('collections', metavar='N', type=str, nargs='+',
                    help='Collection Names')
parser.add_argument('--cols', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Collection Names here like ex: [ col1 col2 --cols ] ')

args = parser.parse_args()
print args.collections
