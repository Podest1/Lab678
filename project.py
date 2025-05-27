import argparse
def parse_args():
 parser = argparse.ArgumentParser(description='Konwerter pilków')
 parser.add_argument('input', help='Plik wejściowy')
 parser.add_argument('output', help='Plik wyjściowy')
 return parser.parse.args()
if __name__ == "__main__":
 args = parse_args()
