import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--site', default='stackoverflow.com', type=str)
    parser.add_argument('prompt', type=str, nargs='+')

    args = parser.parse_args()
    args.prompt = ' '.join(args.prompt)

    return args


if __name__ == '__main__':
    args = parse_args()

    print(args.prompt)
