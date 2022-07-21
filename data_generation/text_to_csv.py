import argparse

def add_titles_to_csv(csv, line):
    category_count = count_categories(line)
    row = []
    for _ in category_count:
        categories = 0

def append_to_csv(csv, line):
    pass

def count_categories(line):
    sum = 0
    words = line.split(":")
    return len(words)

def main(filename):
    csv = []
    with open(filename) as file:
        num_categories = 0
        for line in file:
            if num_categories == 0:
                num_categories = count_categories(line)
            for _ in range(num_categories):
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="Name of the text file to be processed.")
    args = parser.parse_args()
    main(args.filename)