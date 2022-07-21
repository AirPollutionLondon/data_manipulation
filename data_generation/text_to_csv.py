import argparse
from typing import List

def add_categories_to_csv(csv: List[List[str]], line: str) -> None:
    """ Add the headers of each of the categories to the CSV.

        Params:
            - csv: List[List[str]] which represents the csv which will be written to each row is a list
            - line: a line (String) which contains the headers for each column
    """
    columns = line.split(": ")
    row = []
    first_column = True
    for category in columns:
        name_and_data = category.split(" ")
        if first_column:
            row.append(name_and_data[0])
            first_column = False
        elif category == line[len(line) - len(category):]:
            continue
        else:
            row.append(name_and_data[len(name_and_data) - 1])
    csv.append(row)

def add_data_to_csv(csv: List[List[str]], line: str) -> None:
    """ Add the values of each category to the CSV.

        Params:
            - csv: a List[List[str]] which represents the csv which will now have its data filled in
            - line: a line (String) which contains the data of each column
    """
    columns = line.split(": ")
    row = []
    first_column = True
    second_column = False
    for category in columns:
        name_and_data = category.split(" ")
        if first_column:
            second_column = True
            first_column = False
        elif second_column:
            date_time = " ".join([name_and_data[0], name_and_data[1]])
            second_column = False
            row.append(date_time)
        else:
            row.append(name_and_data[0].strip('\n'))
    csv.append(row)

def convert_to_csv(path: str, csv: List[List[str]]) -> None:
    """ Take the csv list and write it into a .csv file.

        Params:
            - path: the path of the original .txt file
            - csv: List[List[str]] to convert to a full file
    """
    with open(path[:len(path) - 4] + ".csv", "w") as new_file:
        for row in csv:
            new_file.write(",".join(row))
            new_file.write("\n")
        new_file.close()

def main(path: str) -> None:
    """ Main method to execute the text file conversion process.

        Params:
            path: A String which represents the path of the text file.
    """
    csv = []
    with open(path) as file:
        csv = []
        skipped = 0
        categories_not_added = True
        for line in file:
            if skipped < 3:
                skipped += 1
                continue
            if categories_not_added:
                add_categories_to_csv(csv, line)
                categories_not_added = False
            add_data_to_csv(csv, line)
        convert_to_csv(path, csv)
        file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="Path of the text file to be processed.")
    args = parser.parse_args()
    main(args.path)