# Informatics INFO-I 210 - Summer 2023

import csv
from string import punctuation


def load_text(file_name: str, output_type: type = list):
    """Load a text file and return its content as a string or a list of strings.

    Args:
        file_name: a string representing the name of a file,
            optionally with paths (which can be system dependent).
        output_type: choose output type (list or str)

    Returns:
        The file's content as a string or as a list of strings.

    Examples:

        >>> load_text("sample_file.txt",str)
        'The file contains this data!'

         >>> load_text("sample_file.txt",list)
        ['The file contains this data!']

    If the file does not exist, this function does not make sense:
    raise an error.
    """
    with open(file_name, "r", encoding="utf-8-sig", newline="") as fh:
        data = fh.read()
        if output_type == str:
            return data
        return data.splitlines()


def write_text(text: str, file_name: str) -> None:
    """Create or overwrite a file and with a string.

    Args:
        text: a string
        file_name: a string representing the name of a file,
            optionally with paths (which can be system dependent).


    Returns:
        None (just writes into a file)

    Examples:

        >>> write_text("My name is Shabnam", "name_file.txt")


    If the file does not exist, this function will create this file.
    """
    with open(file_name, "w", encoding="utf-8-sig", newline="") as fh:
        fh.write(text)


def load_csv(file_name: str, header: bool = True):
    """Load data from a comma-separated value (CSV) file.

    This returns data from a plaintext file where columns
    are represented by values in the first row, and the
    values that those keys take is in the rows which follow.

    If header: The header in a CSV file is turned into keys in
    each dictionary, and the values are the rows.
    Otherwise: Each row will become a list.

    Args:
        file_name: name of the csv file to load from

    Returns:
        If header: A list of disctionaries
        If not: A list of lists

    Notes:

    CSV files are common in science and industry because
    it is often a simple plaintext file that you can send
    to a colleague, download off the internet, and do
    other analysis on.
    """
    with open(file_name, "r", encoding="utf-8-sig", newline="") as csvfile:
        if header:
            return [row for row in csv.DictReader(csvfile)]
        else:
            return [row for row in csv.reader(csvfile)]


def table_print_two_col(headers: list, data: list[list], width: int = 10) -> None:
    """prints a nested list in a double column table format"""
    output = "{:<{}} {:<{}}"
    # print header row
    header1, header2 = headers
    print(output.format(header1, width, header2, width))
    # print dashes to match width (2 cols)
    print("-" * (width + 1) * 2)
    # print out data (2 cols)
    for item1, item2 in data:
        print(output.format(item1, width, item2, width))


def table_print_three_col(headers: list, data: list[list], width: int = 10) -> None:
    """prints a nested list in a double column table format"""
    output = "{:{}} {:{}} {:{}}"
    # print header row
    header1, header2, header3 = headers
    print(output.format(header1, width, header2, width, header3, width))
    # print dashes to match width (2 cols)
    print("-" * (width + 1) * 3)
    # print out data (2 cols)
    for item1, item2, item3 in data:
        print(output.format(item1, width, item2, width, item3, width))


def text_to_list(data: str) -> list:
    """Convert a string of data to a cleaned list of words.

    Examples:

        >>> text_to_list("How are you doing?")
        ['how', 'are','you', 'doing']
    """
    translator = str.maketrans("", "", punctuation)
    return data.lower().translate(translator).split()


# Debugging code for the Module
if __name__ == "__main__":
    pass
